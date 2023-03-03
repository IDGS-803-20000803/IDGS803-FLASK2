from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField,SelectField, RadioField,validators
from wtforms.fields import EmailField 
from wtforms import validators


def mi_validacion(form,field):
    if len(field.data) == 0:
        raise validators.ValidationError("El campo no tiene datos")
class UseForm(Form):
    matricula = StringField('Matricula',[validators.data_required(message="El campo es requerido"),
                                         validators.length(min=4,max=15, message="No cumple la longitud para el campo")])
    nombre = StringField('Nombre',[validators.data_required(message="El campo es requerido")])
    apaterno = StringField('Apaterno',[mi_validacion])
    email = EmailField('Correo')

class LoginForm(Form):
    username = StringField('Usuario',[validators.data_required(message="El campo es requerido"),
                                         validators.length(min=4,max=15, message="No cumple la longitud para el campo")])
    password = StringField('password',[validators.data_required(message="El campo es requerido")])

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

class ResistorForm(Form):
    colors = [('', 'Seleccione una Opcion'),
              ('0', 'Negro'), 
              ('1', 'Marron'),
              ('2', 'Rojo'),
              ('3', 'Naranja'), 
              ('4', 'Amarillo'), 
              ('5', 'Verde'),
              ('6', 'Azul'),
              ('7', 'Violeta'), 
              ('8', 'Gris'), 
              ('9', 'Blanco')]
    band1 = SelectField('Banda 1', choices=colors, validators=[validators.InputRequired('Elija una opcion correcta')])
    band2 = SelectField('Banda 2', choices=colors, validators=[validators.InputRequired('Elija una opcion correcta')])
    multiplier = SelectField('Multiplicador', choices=[('0', 'Negro x1 Ω'), ('1', 'Marron x10 Ω'), 
                                              ('2', 'Rojo x100 Ω'), ('3', 'Naranja x1 kΩ'),
                                              ('4', 'Amarillo x10 kΩ'), ('5', 'Verde x100 kΩ'), 
                                              ('6', 'Azul x1 MΩ'), ('7', 'Violeta x10 MΩ'),
                                              ('8', 'Gris x100 MΩ'), ('9', 'Blanco x10 GΩ')],
                                                       validators=[validators.InputRequired()])
    tolerance = RadioField('Tolerancia', choices=[('oro', 'ORO = 5%'), ('plata', 'PLATA = 10%')], 
                           validators=[validators.InputRequired(message='Este campo no puede quedarse vacio')])                        
