from ast import main
import sys

print('\033[1m''\033[96m'"EJERCICIO 4" '\033[96m''\033[0m')

def error_4(*args):
    resultado=0 #inicamos el contador a 0
    for numero in args: #iniciamos un bucle para que se suma término a término
        #incluimos el try and except para capturar el error
        try:
            resultado=+numero 
            print(resultado) #si todo es correcto se mostrará el resultado

        except TypeError: #En caso contrario, como debe ocurrir, uno de los numeros establecidos no es un número, en vez, serán un caracter tipo string.
            print("No se puede concadenar un 'string' con un 'int'") #Lanzara un mensaje que advirtirá al usuario del error
            #Al incluir TypeError no tenemos porque preocuparnos por añadir el file=sys.stdrr pues estamos utilizando un comando que ya tiene almacena este tipo de error

        finally:#No importa el resultado de la evaluacion, el programa siempre lanzará este mensaje
            return "--OPERACION EVALUADA--"
            sys.exit()#Salimos del try and except

if __name__=="__main__":
    print(error_4("2",10))


