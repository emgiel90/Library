from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from typing import Any



class AddBookForm(FlaskForm):
    """
    Form per aggiungere un libro
    """
    title: Any = StringField('Titolo:', validators=[DataRequired()])
    author: Any = StringField('Autore:', validators=[DataRequired()])
    isbn: Any = StringField('ISBN:', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('Aggiungi il libro')
    
class SearchBookForm(FlaskForm):
    """
    Form per aggiungere un libro
    """
    title: Any = StringField('Titolo:', validators=[DataRequired()])
    submit = SubmitField('Cerca il libro')