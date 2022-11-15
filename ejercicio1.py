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
from ast import main

def Error_1(x,y):
    try:
        x/y
        return "Operacion introducida correctamente"
    except ZeroDivisionError:
        return "Dividir entre 0 no es posible" #al no poder dividir entre 0, controlamos el error mediante un "try" and "except", el cual evalua la division y corrige si se ha dividido por 0.


if __name__=="__main__":
    Error_1(7,0)