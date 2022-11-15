from ast import main

lista = [4, 7, 30, 23, 5]

def error_2(lista):
    try:
        lista[10]
        return "Índice dentro del rango"
    except IndexError:
        