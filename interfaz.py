from flask import Flask, request, render_template, redirect, session
import calculadora as calcu

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/calcu')
def calculator():
    return render_template('calculadora.html')

@app.route('/identificar_operacion', methods=['POST'])
def identificar_operacion():
    if request.method == 'POST':
        operacion = request.form.get('operacion')
        numeros_input = request.form.get('inputNumbers')
        
        numeros = numeros_input.split()
        
        # Almacena la operación en la sesión
        session['operacion'] = operacion
        
        return render_template('calculadora.html', input_numbers=numeros_input, operacion=operacion) 

@app.route('/realizar_operacion', methods=['POST'])
def realizar_operacion():
    if request.method == 'POST':
        numeros_input = request.form.get('inputNumbers')
        operacion = session.get('operacion', 'igual')  # Obtén la operación almacenada en la sesión
        
        numeros = numeros_input.split()
        
        calculadora = calcu.Calculadora(numeros[0], numeros[1])
        
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
            
        return render_template('calculadora.html', input_numbers=f"{numeros[0]} {numeros[1]} {resultado}", operacion=operacion) 


if __name__ == '__main__':
    app.run(debug=True)
