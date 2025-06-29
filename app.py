from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from models import db, User, DailyReport
from forms import RegistrationForm, LoginForm, DailyReportForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from datetime import date, datetime, timedelta
import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---- User Registration ----
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, real_name=form.real_name.data,
                    email=form.email.data, telephone=form.telephone.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration submitted. Awaiting admin approval.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# ---- User Login ----
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            if not user.approved:
                flash('Account not yet approved by admin.')
                return redirect(url_for('login'))
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# ---- Home ----
@app.route('/')
@login_required
def index():
    return render_template('index.html')

# ---- Daily Report Form ----
@app.route('/report', methods=['GET', 'POST'])
@login_required
def report():
    form = DailyReportForm()
    # Remove already selected option for second dropdown
    if form.line_job_card_1.data:
        form.line_job_card_2.choices = [(i, str(i)) for i in range(1, 15) if i != form.line_job_card_1.data]
    if form.validate_on_submit():
        if form.submit.data:
            dr = DailyReport(
                user_id=current_user.id,
                date=date.today(),
                good_garment_total=form.good_garment_total.data,
                defeat_total=form.defeat_total.data,
                line_job_card_1=form.line_job_card_1.data,
                line_job_card_2=form.line_job_card_2.data,
                test1=form.test1.data,
                test2=form.test2.data,
                test3=form.test3.data,
                test4=form.test4.data,
                test5=form.test5.data,
                test6=form.test6.data,
                test7=form.test7.data,
                test8=form.test8.data,
                test9=form.test9.data,
                test10=form.test10.data
            )
            db.session.add(dr)
            db.session.commit()
            flash('This is being sent to Q.M Subhash Jayawardhana. Send only if correct.', 'warning')
            return redirect(url_for('index'))
        elif form.clear.data:
            return redirect(url_for('report'))
    return render_template('report.html', form=form)

# ---- Admin Panel ----
@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if not current_user.is_admin:
        flash('Admins only.')
        return redirect(url_for('index'))

    unapproved_users = User.query.filter_by(approved=False).all()
    if request.method == 'POST':
        for user_id in request.form.getlist('approve'):
            user = User.query.get(int(user_id))
            if user:
                user.approved = True
        db.session.commit()
        flash('Selected users approved!')
        return redirect(url_for('admin'))

    return render_template('admin.html', unapproved_users=unapproved_users)

# ---- Admin Charts ----
@app.route('/admin/charts')
@login_required
def charts():
    if not current_user.is_admin:
        flash('Admins only.')
        return redirect(url_for('index'))

    period = request.args.get('period', 'daily')
    today = date.today()
    if period == 'daily':
        start_date = today
    elif period == 'weekly':
        start_date = today - timedelta(days=7)
    else:  # monthly
        start_date = today - timedelta(days=30)

    reports = DailyReport.query.filter(DailyReport.date >= start_date).all()
    # Prepare data for top 5 lines
    line_stats = {}
    for report in reports:
        line = report.line_job_card_1
        if report.defeat_total and report.defeat_total > 0:
            val = 100 * (report.test1 / report.defeat_total)
        else:
            val = 0
        if line not in line_stats:
            line_stats[line] = []
        line_stats[line].append(val)
    top5 = sorted([(k, sum(v)/len(v) if v else 0) for k, v in line_stats.items()], key=lambda x: x[1], reverse=True)[:5]
    return render_template('charts.html', top5=top5, period=period)

if __name__ == '__main__':
    app.run(debug=True)
