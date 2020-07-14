from random import randint

salida = False

print("Binvendio a practica de calculo mental")
while salida == False:
    print("1.Suma\n2.Restas\n3.Multipliación\n4.Salir")
    opcion = int(input())

    if opcion == 1:
        print("Nivel 1:")
        contador = 0
        for i in range(0, 5, 1):
            num1 = randint(0, 9)
            num2 = randint(0, 9)
            print(num1, " + ", num2, " = ")
            result = int(input())
            if result == (num1+num2):
                contador += 1

        if contador == 5:
            print("Pasaste al nivel 2:")
            contador = 0
            for i in range(0, 5, 1):
                num1 = randint(0, 9)
                num2 = randint(0, 99)
                print(num1, " + ", num2, " = ")
                result = int(input())
                if result == (num1+num2):
                    contador += 1