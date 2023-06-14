from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from app.models import User, CourseDesc
from flask_login import current_user


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')


class DescForm(FlaskForm):
    coursename = StringField('Course Name', validators=[DataRequired()])
    body = StringField('Course Description', validators=[DataRequired()])
    submit = SubmitField('Add Course Description')


class CommentForm(FlaskForm):
    studentname = StringField('Student Name', validators=[DataRequired()])
    studentgrade = IntegerField('Student Mark', validators=[DataRequired()])
    
    def get_user_courses():
        return CourseDesc.query.filter_by(author=current_user)
    
    body = QuerySelectField('Course Description', query_factory=get_user_courses, get_label='body', validators=[DataRequired()])
    submit = SubmitField('Generate Comment')