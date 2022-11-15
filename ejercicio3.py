
# 3) Código a evaluar:
import sys
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
def error_3(paises):
    try:
        paises["alemania"]
    except KeyError:
        print("Clave no encontrada dentro del diccionario",file=sys.stderr)
        sys.exit()

error_3(paises)

#El error en este tercer código es que no podemos encontrar la clave alemania dentro del diccionario, por consiguiente no podemos encontrar su valor; ya que ninguno de los dos está definido. Al ejecutarlo nos saltará el error "KeyError"; para solucinarlo utilizaremos "try" y "except". Dentro de la función "try" introduciremos aquello que queremos probar; si el resultado no se puede ejecutar directamente pasará al "except" donde, si el tipo de error, es el que nosotros hemos indicado se imprimirá por pantalla aquello que hay dentro del "except"
print("\n\n")



