from ast import main
import sys

print('\033[1m''\033[96m'"EJERCICIO 4" '\033[96m''\033[0m')

def error_4(*args):
    resultado=0
    for numero in args:
        try:
            resultado=+numero
            print(resultado)
        except TypeError:
            print("Se ha introducido un caracter que no es un numero")
        finally:
            return "--OPERACION EVALUADA--"
            sys.exit()

if __name__=="__main__":
    print(error_4("2",10))


