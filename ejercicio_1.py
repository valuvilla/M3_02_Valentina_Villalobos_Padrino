from ast import main
import sys
x=7
y=0
def error_1(x,y):
    try:
        codigo=x/y
    except ZeroDivisionError:
        print("Dividir entre 0 no es posible", file=sys.stderr)
    finally:
        return "Operacion evaluada"

if __name__=="__main__":
    main()
