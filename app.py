from flask import Flask, render_template
from flask import request
import forms
from collections import Counter
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
    app.run(debug=True)