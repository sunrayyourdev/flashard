from wtforms import Form, validators, StringField

class DeckForm(Form):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=150)])