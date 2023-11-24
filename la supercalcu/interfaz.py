from flask import Flask, request, render_template, redirect, session
from calculadora import Calculadora

app = Flask(__name__)
app.secret_key = 'secret_key'

#función básica de la página principal
@app.route('/calcu')
def calculator():
    return render_template('calculadora.html', resultado=session.get('resultado', None))

@app.route('/realizar_operacion', methods=['POST'])
def realizar_operacion():
    if request.method == 'POST':
        #coge los número y la operación de la página html
        numero1 = request.form.get('numero1')
        numero2 = request.form.get('numero2')
        operacion = request.form.get('operacion')

        # Almacena la operación en la sesión
        session['operacion'] = operacion

        #creamos un objeto de la clase Calculadora, con los números que hemos cogido de la página html
        calculadora = Calculadora(numero1, numero2)

        #dependiendo de la operación que se haya elegido, llama a una función u otra de la clase Calculadora
        resultado = None
        if operacion == 'sumar':
            resultado = calculadora.suma()
        elif operacion == 'restar':
            resultado = calculadora.resta()
        elif operacion == 'multiplicar':
            resultado = calculadora.multiplicacion()
        elif operacion == 'dividir':
            resultado = calculadora.division()
        else:
            resultado = "Operacion no reconocida"

        # Almacena el resultado en la sesión
        session['resultado'] = resultado
        
        #Envía a la página html el resultado de la operación
        mensaje = "El resultado de la operacion es: " + str(resultado)
        return render_template('calculo_hecho.html', mensaje=mensaje)
    
