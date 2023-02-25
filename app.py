from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from collections import Counter
from flask import make_response
from flask import flash
import forms
import diccionario
import actividad2



app =Flask(__name__)
'''
app.config['SECRET_KEY'] = "Esta es la clave encriptada"
csrf = CSRFProtect()
'''
@app.route('/Diccionario', methods=['GET', 'POST'])
def index():
    formGuardar = actividad2.GuardarForm(request.form)
    formBuscar = actividad2.BuscarForm(request.form)
    result = ''

    # Si se presiona el boton de guardar
    if request.method == 'POST' and 'guardar' in request.form:
        if formGuardar.validate():
            espanolP = formGuardar.espanol.data.upper()
            inglesP = formGuardar.ingles.data.upper()

            # Guarda la informacion en el archivo de texto
            with open('diccionario.txt', 'a') as file:
                file.write(espanolP + '=' + inglesP + '\n')
    if request.method == 'POST' and 'limpiar' in request.form:
       return render_template('diccionario.html', formGuardar=formGuardar, formBuscar=formBuscar, result=result)
    # Si se presiona el boton de buscar
    if request.method == 'POST' and 'buscar' in request.form:
        if formBuscar.validate():
            palabraBuscar = formBuscar.palabra_buscar.data.upper()
            idioma = formBuscar.respuesta.data

            # Busca la informacion en el archivo de texto
            with open('diccionario.txt', 'r') as file:
                for line in file:
                    spanish, english = line.strip().split('=')
                    if idioma == 'es' and spanish == palabraBuscar:
                        result = english
                        break
                    elif idioma == 'en' and english == palabraBuscar:
                        result = spanish
                        break
                else:
                    result = 'Palabra no encontrada'
    if request.method == 'POST' and 'limpiar' in request.form:
       return render_template('actividad2.html', formGuardar=formGuardar, formBuscar=formBuscar, result=result)
    return render_template('actividad2.html', formGuardar=formGuardar, formBuscar=formBuscar, result=result)


@app.errorhandler(404)
def no_encontrada(e):
        return render_template('404.html'), 404

@app.route("/cookies", methods=['GET','POST'])
def cookies():
    reg_user = forms.LoginForm(request.form)
    datos=''
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        passw = reg_user.password.data
        datos = user + '@'+passw
        succes_message = 'Bienvenido {}'.format(user)
        flash(succes_message)
    response=make_response(render_template('cookies.html', form = reg_user))
    if len(datos)> 0:
        response.set_cookie('datos_user',datos)
    return response

@app.route("/saludo")
def saludo():
    valor_cookie = request.cookies.get('datos_user')
    nombres = valor_cookie.split('@')
    return render_template('saludo.html', nom = nombres[0])



@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
    alum_form = forms.UseForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
    return render_template("Alumnos.html", form = alum_form)

@app.route('/')
def form():
    return render_template('Principal.html')
           
@app.route("/resultado", methods = ['GET', 'POST'])
def process():
    if request.method == 'POST':
        numberFields = int(request.form.get('txtNum'))
        return render_template('Dinamicas.html', numberFields = numberFields)
    


@app.route("/calcular", methods = ['GET', 'POST'])
def calcular():
  
  numbersString = request.form.getlist('txtNum')
  numbersInt = list(map(int, numbersString))

  major = max(numbersInt)
  minor = min(numbersInt)

  average = sum(numbersInt) / len(numbersInt)

  for i in range(len(numbersString)):
        numbersString[i] = int(numbersString[i])

  counter = Counter(numbersString)
  resultados = counter.most_common()
  results = []
  for r in resultados:
        if r[1] > 1:
            results.append('El numero {0} se repite {1}'.format(r[0], r[1]))
 

  return render_template('resultado.html', major = major, minor = minor, average = average, results = results)

if __name__ == "__main__":
    '''
    csrf.init_app(app)
    '''
    app.run(debug=True)