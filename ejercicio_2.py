from ast import main
import sys

lista = [4, 7, 30, 23, 5]

def error_2(lista):
    try:
        lista[10]
    except IndexError:
        print("Índice fuera de rango",file=sys.stderr)
        sys.exit()
    finally:
        return "--BÚSQUEDA EVALUADA--"

if __name__=="__main__":
    main()