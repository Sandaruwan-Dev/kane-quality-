from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    real_name = StringField('Real Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telephone = StringField('Telephone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class DailyReportForm(FlaskForm):
    good_garment_total = IntegerField('Good Garment Total', validators=[DataRequired()])
    defeat_total = IntegerField('Defeat Total', validators=[DataRequired()])
    line_job_card_1 = SelectField('Line Job Card 1', coerce=int, choices=[(i, str(i)) for i in range(1, 15)], validators=[DataRequired()])
    line_job_card_2 = SelectField('Line Job Card 2', coerce=int, choices=[(i, str(i)) for i in range(1, 15)], validators=[DataRequired()])
    test1 = IntegerField('Testing 1', validators=[DataRequired()])
    test2 = IntegerField('Testing 2', validators=[DataRequired()])
    test3 = IntegerField('Testing 3', validators=[DataRequired()])
    test4 = IntegerField('Testing 4', validators=[DataRequired()])
    test5 = IntegerField('Testing 5', validators=[DataRequired()])
    test6 = IntegerField('Testing 6', validators=[DataRequired()])
    test7 = IntegerField('Testing 7', validators=[DataRequired()])
    test8 = IntegerField('Testing 8', validators=[DataRequired()])
    test9 = IntegerField('Testing 9', validators=[DataRequired()])
    test10 = IntegerField('Testing 10', validators=[DataRequired()])
    submit = SubmitField('Submit')
    clear = SubmitField('Clear All')
