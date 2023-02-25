from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, validators
from wtforms import validators

# Define la clase del formulario para la seccion de guardar
class GuardarForm(Form):
    espanol = StringField('Espanol', [
        validators.DataRequired(message='Es necesario ingresar una palabra en espanol'),
        validators.InputRequired()])
    ingles = StringField('Ingles', [ 
        validators.DataRequired(message='Es necesario ingresar una palabra en ingles'),
         validators.InputRequired()])

# Define la clase del formulario para la seccion de busqueda
class BuscarForm(Form):
    palabra_buscar = StringField('Palabra', [ 
        validators.DataRequired(message='Es necesario ingresar una palabra para realizar la busqueda'),
        validators.InputRequired()])
    respuesta = RadioField('Idioma de busqueda', choices=[('es', 'Espanol'), ('en', 'Ingles')],
        validators=[validators.InputRequired(message='Seleccione una opcion')])