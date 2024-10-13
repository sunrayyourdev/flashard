from wtforms import Form, validators, StringField


class DeckForm(Form):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=150)])


class UpdateDeckForm(Form):
    old_name = StringField('Old Name', [validators.DataRequired(), validators.Length(min=1, max=150), validators.Disabled()])
    new_name = StringField('New Name', [validators.DataRequired(), validators.Length(min=1, max=150)])