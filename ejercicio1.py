"""
Identificar los errores en los siguiente bloques de código y 
evaluarlos con excepciones especificas para evitar errores no 
controlados en nuestros programas. 
Añade mensajes explicativos para el usuario.
Nota: Se tienen que evaluar excepciones concretas, 
no hacer referencia a Exception sin más.
1) Código a evaluar:
numero = 7/0
2) Código a evaluar:
lista = [4, 7, 30, 23, 5]
lista[10]
3) Código a evaluar:
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
paises["alemania"]
4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
resultado = "2" + 10
"""
x=7
y=0
import sys

def Error_1(x,y):
    try:
        x/y
        return "Operacion terminada"
    except ZeroDivisionError:
        return "La operacion no ha sido realizada"
#El error en este primer código es que no podemos dividir un número entre 0 ya que no está definido. Al ejecutarlo nos saltará el error "ZeroDivisionError"; para solucinarlo utilizaremos "try" y "except". Dentro de la función "try" introduciremos aquello que queremos probar; si el resultado no se puede ejecutar directamente pasará al "except" donde, si el tipo de error, es el que nosotros hemos indicado se imprimirá por pantalla aquello que hay dentro del "except"
print(Error_1(x,y))