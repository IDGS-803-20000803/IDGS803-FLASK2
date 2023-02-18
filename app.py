from flask import Flask, render_template
from flask import request
import forms
app =Flask(__name__)

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
    alum_form = forms.UseForm(request.form)
    if request.method == 'POST':
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
    return render_template("Alumnos.html", form = alum_form)



@app.route('/')
def form():
    return render_template('Principal.html')
           
@app.route("/resultado", methods = ['GET', 'POST'])
def process():
    if request.method == 'POST':
        fields = int(request.form.get('txtNum'))

        return render_template('Dinamicas.html', fields = fields)
    elif request.method == 'GET':
        return render_template('') 
    
    return render_template('Principal.html')

if __name__ == "__main__":
    app.run(debug=True)