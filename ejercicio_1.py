
from ast import main
import sys

print('\033[1m''\033[96m'"EJERCICIO 1" '\033[96m''\033[0m')

def error_1(x,y):
    #Uso de try and except para controlar las excepciones
    
    try:
        x/y#se evalua la division


    except ZeroDivisionError: #Controlamos que el denominador no sea 0 mediante ZeroDivisionError que permite que el programa lo dectecte
        print("Dividir entre 0 no es posible") #cuando se divide entre cero, el programa lanzara este mensaje. Además de que se guardará el error mediante el file=sys.stderr
        
    finally: #No importa el resultado de la evaluacion, el programa siempre lanzará este mensaje
        return "--OPERACION EVALUADA--"
        sys.exit() #Salimos del try and except



if __name__=="__main__":
   print(error_1(7,0))
