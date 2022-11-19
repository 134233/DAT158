from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    """
    The form for entering values.
    """

    budget = IntegerField('Budget: ', validators=[NumberRange(min=0, max=50000000)])

    genres = StringField('Genre: ', validators=[DataRequired()])

    release_year = IntegerField('Release year: ', validators=[NumberRange(min=1850, max=2022)])

    cast = StringField('Cast: ', validators=[DataRequired()])

    submit = SubmitField('Submit')