from ast import main
import sys

print('\033[1m''\033[96m'"EJERCICIO 3" '\033[96m''\033[0m')

paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 

def error_3(paises):

    #incluimos el try and except para capturar el error
    try:
        paises["alemania"] #se accede al valor de una clave dada

    except KeyError: #En caso de no encontrario, se emplea el KeyError que ya almacena el error para corregir el error
        print("Clave-valor no encontrada") #Lanzara un mensaje que advirtirá al usuario del error
        #Al incluir el KeyError no tenemos porque preocuparnos por añadir el file=sys.stdrr pues estamos utilizando un comando que ya tiene almacena este tipo de error

    finally:#No importa el resultado de la evaluacion, el programa siempre lanzará este mensaje
        return "--BÚSQUEDA DE CLAVE-VALOR EVALUADA--"
        sys.exit()#Salimos del try and except


#Experimentamos con en ejemplo
print(error_3(paises))

if __name__=="__main__":
    main()
