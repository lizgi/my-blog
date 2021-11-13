from wtforms import StringField,TextAreaField, SubmitField, SelectField 
from wtforms.validators import Required, Email, Length
from flask_wtf import FlaskForm


class BlogForm(FlaskForm):
    blog_title = StringField('Blog title', validators=[Required()])
    category = SelectField('Blog category',choices=[('Select a category','Select a category'),('Fashion', 'Fashion'),('Sports','Sports'),('Travel','Travel'),('Tech','Tech')], validators=[Required()])
    content = TextAreaField('Body', validators=[Required()])
    created_by= StringField('Blog author',validators=[Required()])
    submit = SubmitField('Submit')