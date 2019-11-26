from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    category = SelectField('Select Category', choices=[('Music', 'Music'), ('Techies', 'Techies'), ('Puns', 'Puns')])
    description=TextAreaField('Your Post', validators=[Required()])
    author=StringField('Your Name', validators=[Required()])
    submit =SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = StringField('Your Comment', validators=[Required()])
    user=StringField('Your Name', validators=[Required()])
    submit=SubmitField('Submit')
