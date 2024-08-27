from wtforms import Form, validators, StringField, EmailField, PasswordField

# TODO: Make forms here
class ExampleForm(Form):
    attribute = StringField('', [validators.DataRequired(), validators.Length(min=1, max=150)])