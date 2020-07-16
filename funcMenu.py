from math import pi

def segundos(segundos):
    print("Se puede convertir a: ")
    dias = segundos // 86400
    segundos = segundos - (dias * 86400)
    horas = segundos // 3600
    segundos = segundos - (horas * 3600)
    minutos = segundos // 60
    segundos = segundos - (minutos * 60)

    print (f"dias: {dias}")
    print (f"horas: {horas}")
    print (f"minutos: {minutos}")
    print (f"segundos: {segundos}")

def piesToCm(pies):
    result = pies * 30.48
    return result

def volumenEsfera(radio):
    resultado = (4/3)*pi*(radio**3)
    return resultado

def multiploDe(comprobar, divisor):
    if (comprobar % divisor) == 0:
        return True
    else:
        return False

def compara(num1, num2):
    if num1 < num2:
        return -1
    elif num1 == num2:
        return 0
    else:
        return 1

opcion = 0

while opcion != 6:
    print("\nMENU FUNCIONES\nIngrese el numero de la opcione que desea: ")
    print("1.Sgundos a dias horas y minutos\n2.Pies a CM\n3.Volumen de una Esfera\n4.Multiplo de\n5.Compara dos valores\n6.Salir")
    opcion = int(input())

    if opcion == 1:
        secs = int(input("Dame los segundos: "))
        segundos(secs)
    elif opcion == 2:
        feet = float(input("Dame la medida en pies: "))
        resultado = piesToCm(feet)

        print("En cm es: ", resultado)
    elif opcion == 3:
        rad = float(input("Dame el radio: "))
        result = volumenEsfera(rad)

        print("El volumen es: ", result)
    elif opcion == 4:
        num1 = int(input("Ingrese el valor 1: "))
        num2 = int(input("Ingrese el valor 2: "))

        result = multiploDe(num1, num2)

        print("El numero es multiplo: ", result)
    elif opcion == 5:
        nume1 = int(input("Dame el num1 a comparar: "))
        nume2 = int(input("Dame el num2 a comparar: "))

        result = compara(nume1, nume2)
        print("regresa: ", result)
    elif opcion == 6:
        opcion = opcion
    else:
        print ("Esa opcion no existe")

