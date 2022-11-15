from ast import main
import sys

paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 


def error_3(paises):

    try:
        paises["alemania"]

    except KeyError:
        print("Clave-valor no encontrada")
        sys.exit()

    finally:
        return "BÚSQUEDA DE CLAVE-VALOR EVALUADA"


print(error_3(paises))
if __name__=="__main__":
    main()
