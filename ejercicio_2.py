
from ast import main
import sys

print('\033[1m''\033[96m'"EJERCICIO 2" '\033[96m''\033[0m')

lista = [4, 7, 30, 23, 5]

def error_2(lista):
    #Uso de try and except para controlar las excepciones
    try:
        lista[10] #reccorremos la lista en busca del elemento de posicion 11
    
    except IndexError: #En caso de que el indice dado se exceda a la longitud de la lista, hacemos uso de IndexError para controlar esta excepcion
        print("Índice fuera de rango") #Lanzara un mensaje que advirtirá al usuario del error
        #Al incluir IndexError no tenemos porque preocuparnos por añadir el file=sys.stdrr pues estamos utilizando un comando que ya tiene almacena este tipo de error


    finally: #No importa el resultado de la evaluacion, el programa siempre lanzará este mensaje
        return "--BÚSQUEDA DE ÍNDICE EVALUADA--"
        sys.exit()#Salimos del try and except

#Experimentamos con en ejemplo
print(error_2(lista))

if __name__=="__main__":
    main()