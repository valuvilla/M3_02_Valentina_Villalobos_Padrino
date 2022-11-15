
from ast import main


lista = [4, 7, 30, 23, 5]
def error2(lista):
    try:
        lista[10]
        return "Indice dentro del rango"
    except IndexError:
        return "Índice fuera del rango"

print(error2(lista))


if __name__=="__main__":
    main()