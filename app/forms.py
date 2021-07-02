from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class TodoForm(FlaskForm):
    description = StringField(None, validators=[DataRequired()])
    submit = SubmitField('Add')


class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Remove')


class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Update')
