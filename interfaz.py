from flask import Flask, request, render_template, redirect
import calculadora as calcu

app = Flask(__name__)

@app.route('/calcu')
def calculator():
    return render_template('calcuradora.html')

@app.route('/identificar_operacion', methods=['POST'])
def identificar_operacion():
    if request.method == 'POST':
        operacion = request.form.get('operacion')
        numeros_input = request.form.get('inputNumbers')
        
        numeros = numeros_input.split()
        
        calculadora = calcu(numeros[0], numeros[1])
        
        if operacion == 'suma':
            resultado = calculadora.suma()        
        elif operacion == 'resta':
            resultado = calculadora.resta()
        elif operacion == 'multiplicacion':
            resultado = calculadora.multiplicacion()
        elif operacion == 'division':
            resultado = calculadora.division()
        else: 
            resultado = "Operacion no reconocida"
            
        return render_template('calcuradora.html', resultado=resultado) 
