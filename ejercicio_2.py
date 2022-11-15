from ast import main
import sys

lista = [4, 7, 30, 23, 5]

def error_2(lista):
    #Uso de try and except para controlar las excepciones
    try:
        lista[10] #reccorremos la lista en busca del elemento de posicion 11
    
    
    except IndexError: #En caso de que el indice dado se exceda a la longitud de la lista, hacemos uso de IndexError para controlar esta excepcion
        print("Índice fuera de rango",file=sys.stderr) #Lanzara un mensaje que advirtirá al usuario del error, ademas de almacenar el error.
        sys.exit()#Salimos del try and except

    
    finally: #No importa el resultado de la evaluacion, el programa siempre lanzará este mensaje
        return "--BÚSQUEDA DE ÍNDICE EVALUADA--"



if __name__=="__main__":
    main()