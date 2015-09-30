from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Length,
                                EqualTo)



class PostForm(Form):
    contains_message = ("Post name must contain only letters," +
                            "numbers and underscores")

    post_name = StringField('Blog Post Name:',
                            validators=[
                                DataRequired(),
                                Regexp(r'[a-z0-9A-Z_]+$',
                                        message = contains_message)
                            ])
    post_content = TextAreaField('Type your content here',
                                    validators=[DataRequired()])
