
from ast import main
import sys

print('\033[1m''\033[96m'"EJERCICIO 1" '\033[96m''\033[0m')
x=7
y=0
def error_1(x,y):
    #Uso de try and except para controlar las excepciones
    
    try:
        x/y#se evalua la division


    except ZeroDivisionError: #Controlamos que el denominador no sea 0 mediante ZeroDivisionError que permite que el programa lo dectecte
        print("Dividir entre 0 no es posible") #cuando se divide entre cero, el programa lanzara este mensaje. Además de que se guardará el error mediante el file=sys.stderr
        #Al incluir ZeroDivisionError no tenemos porque preocuparnos por añadir el file=sys.stdrr pues estamos utilizando un comando que ya tiene almacena este tipo de error


    finally: #No importa el resultado de la evaluacion, el programa siempre lanzará este mensaje
        return "--OPERACION EVALUADA--"
        sys.exit() #Salimos del try and except


#Experimentamos con en ejemplo


if __name__=="__main__":
   main()