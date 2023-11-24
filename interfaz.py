from flask import Flask, request, render_template, redirect, session
from calculadora import Calculadora

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/calcu')
def calculator():
    return render_template('calculadora.html')

@app.route('/realizar_operacion', methods=['POST'])
def realizar_operacion():
    if request.method == 'POST':
        numero1 = request.form.get('numero1')
        numero2 = request.form.get('numero2')
        operacion = request.form.get('operacion')

        # Almacena la operación en la sesión
        session['operacion'] = operacion

        calculadora = Calculadora(numero1, numero2)

        resultado = None
        if operacion == 'sumar':
            resultado = calculadora.suma()
        elif operacion == 'restar':
            resultado = calculadora.resta()
        elif operacion == 'multiplicar':
            resultado = calculadora.multiplicacion()
        elif operacion == 'division':
            resultado = calculadora.division()
        else:
            resultado = "Operacion no reconocida"

        return render_template('calculadora.html', numero1=numero1, numero2=numero2, resultado=resultado, operacion=operacion)

if __name__ == '__main__':
    app.run(debug=True)
