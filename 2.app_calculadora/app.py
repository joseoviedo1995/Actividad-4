#importamos las clases y metodos 
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST']) 
def aritmetica():
    if request.method == "POST":
        #Valores recividos del form n1,n2 son pasados
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))
        #Realizamos operaciones aritmeticas
        suma = num1 + num2
        resta = num1- num2
        multiplicacion = num1 * num2
        divicion = num1 / num2
        return render_template('index.html', total_suma=suma,
                                             total_resta=resta,
                                             total_multiplicacion=multiplicacion,
                                             total_divicion=divicion )
    return render_template('index.html')

@app.route('/conversion', methods=['GET', 'POST']) 
def conversion():
    if request.method == "POST":
        #Valores recividos del form med son pasados
        me = float(request.form.get('me'))
        
        #Realizamos operaciones aritmeticas
        kilometros = me / 1000
        centimetros = me * 100
        milimetros = me * 1000
        decimetros = me *10
        
        return render_template('conversion.html', total_kilometro= kilometros,
                                             total_centimetros= centimetros,
                                             total_milimetros= milimetros,
                                             total_decimetros= decimetros )
    return render_template('conversion.html')

if __name__ =="__main__" :
    app.run(debug=True)
    