# antipatrones

https://github.com/AnaLopezP/antipatrones

## Identificación características Spaghetti code en el código:

Para mejorar este código, habría que establecer una estructura más clara, con funciones más pequeñas, así si el código crece no se dificulta la comprensión y el mantenimiento.

Por otra parte, el uso del print() para mensajes de error no es una buena práctica, es mejor levantar una excepción, para que el código pueda manejar los errores de manera más efectiva.

Otros errores en el código son: la falta de verificación antes de realizar las operaciones. Podría ser útil verificar si la operación proporcionada es válida. Por último, aunque es un código corto, haría falta documentarlo para facilitar la comprensión del funcionamiento del código.

## Justificación de los cambios

He pasado la única función a una clase Calculadora, la cual se inicializa con dos números, y tiene una función por operación. De esta manera, he organizado el código de una manera que se puedes genstionar bien los errores. Si en algún momento se quiere aumentar el número de operaciones o de atributos, se puede hacer de una manera sencilla, sin riesgo a estropear el resto de código ya hecho. 
