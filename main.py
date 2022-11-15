print('\033[1m''\033[96m'"EJERCICIO 1" '\033[96m''\033[0m')
import ejercicio_1

print('\033[1m''\033[33m'"EJERCICIO 2" '\033[33m''\033[0m')
import ejercicio2

"""
print("\n\n")

# 1) Código a evaluar:

x=7
y=0

try:
  numero=7/0
except ZeroDivisionError:
    print("No se ha podido realizar la división")


#El error en este primer código es que no podemos dividir un número entre 0 ya que no está definido. Al ejecutarlo nos saltará el error "ZeroDivisionError"; para solucinarlo utilizaremos "try" y "except". Dentro de la función "try" introduciremos aquello que queremos probar; si el resultado no se puede ejecutar directamente pasará al "except" donde, si el tipo de error, es el que nosotros hemos indicado se imprimirá por pantalla aquello que hay dentro del "except"
print("\n\n")




# 2) Código a evaluar:

lista = [4, 7, 30, 23, 5]

try:
  lista[10]
except IndexError:
  print("El índice de la lista se encuentra fuera del rango")


#El error en este segundo código es que no podemos encontrar la posición 11 de ls lista  ya que no está definida. Al ejecutarlo nos saltará el error "IndexError"; para solucinarlo utilizaremos "try" y "except". Dentro de la función "try" introduciremos aquello que queremos probar; si el resultado no se puede ejecutar directamente pasará al "except" donde, si el tipo de error, es el que nosotros hemos indicado se imprimirá por pantalla aquello que hay dentro del "except"
print("\n\n")




# 3) Código a evaluar:

paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 

try:
  paises["alemania"]
except KeyError:
  print("Clave no encontrada dentro del diccionario")


#El error en este tercer código es que no podemos encontrar la clave alemania dentro del diccionario, por consiguiente no podemos encontrar su valor; ya que ninguno de los dos está definido. Al ejecutarlo nos saltará el error "KeyError"; para solucinarlo utilizaremos "try" y "except". Dentro de la función "try" introduciremos aquello que queremos probar; si el resultado no se puede ejecutar directamente pasará al "except" donde, si el tipo de error, es el que nosotros hemos indicado se imprimirá por pantalla aquello que hay dentro del "except"
print("\n\n")




#  EJERCICIO 4

  # resultado= "2" + 10
  # El error en este bloque de código es que estamos tratando de sumar una cadena de texto con un número entero. Cuando ponemos entre comillas un número, el programa lo detecta como si fuera un "string" y no podemos sumarlo. Para arreglarlo haremos lo mismo que en los tres códigos anteriores.

num1= "2"
num2=10

try:
  resultado="2" + 10
except TypeError:
  print("No se pudo realizar la operación debido a que los tipos de datos son incorrectos")
  """