from random import randint

noches = int(input("¿Cuántas noches se hospedará en Hard Rock Nuevo Vallarta?\n"))
bono = 0
opcion = 0

contKayak = 0
contBanana = 0
contMasaje = 0
contVapor = 0

if noches <= 0:
    print("No se está registrando para ninguna noche.")
elif noches >= 3:
    bono = 1450
    print("Usted aplica para un bono de 1450dlls para ser utilizado en actividades del hotel")
    while opcion != 4:
        print("Hard Rock Nuevo Vallarta - Menu de amenidades:")
        print("----------------------------------------------")
        print("CREDITO: ", bono)
        print("----------------------------------------------")
        print("1.Paseos\n2.Spa\n3.Juego en linea\n4.SALIR")
        opcion = int(input("Ingrese el numero de la opción que desea:\n"))

        if opcion == 1:
            print("\nEliga de los siguientes paseos:\n1.Paseo en Kayak - $500\n2.Paseo en banana - $250")
            opcion = int(input())
            if opcion == 1 and bono >= 500:
                print("Disfrute del paseo")
                bono = bono - 500
                contKayak += 1
            elif opcion == 2 and bono >= 250:
                print("Disfrute del paseo")
                bono = bono - 250
                contBanana += 1
            elif (opcion == 1 and bono < 500) or (opcion == 2 and bono < 250):
                print("Su saldo no es el suficiente")
        elif opcion == 2:
            print("\nEliga uno de los siguientes servicios:\n1.Masajes - $600\n2.Vapor - $300")
            opcion = int(input())
            if opcion == 1 and bono >= 600:
                print("Disfrute del masaje")
                bono = bono - 600
                contMasaje += 1
            elif opcion == 2 and bono >= 300:
                print("Disfrute del vapor")
                bono = bono - 300
                contVapor += 1
            elif (opcion == 1 and bono < 600) or (opcion == 2 and bono < 300):
                print("Su saldo no es el suficiente")
        elif opcion == 3:
            numeroRandom = randint(0, 100)
            contador = 8
            ganador = False

            print("BIENVENIDO AL ADIVINADOR 3000\nEscoge un numero entre 0 y 100")
            while contador > 0:
                print("Le quedan ", contador, " intentos")
                escogido = int(input("Ingrese un numero:\n"))
                if escogido == numeroRandom:
                    print("¡Felicidades! Gano un pase para la noche casino.")
                    print("Le tomó ", (8 - contador + 1), " intentos")
                    contador = 0
                    ganador = True
                elif escogido < numeroRandom:
                    print("El numero a adivinar es mayor")
                elif escogido > numeroRandom:
                    print("El numero a adivinar es menor")
                contador -= 1
            if ganador == False:
                print("Se le agotaron los intentos. Intente de nuevo. Su numero era: ", numeroRandom, "\n")

    if bono < 1450:
        if contKayak > 0:
            print("Usted utlizo el servicio de Paseo en kayak ", contKayak, " veces ", " con un costo total de: ",contKayak * 500)
        if contBanana > 0:
            print("Usted utlizo el servicio de Paseo en banana ", contBanana, " veces ", " con un costo total de: ",contBanana * 250)
        if contMasaje > 0:
            print("Usted utlizo el servicio de masaje ", contMasaje, " veces ", " con un costo total de: ", contMasaje * 600)
        if contVapor > 0:
            print("Usted utlizo el servicio de vapor ", contVapor, " veces ", " con un costo total de: ", contVapor * 300)
        print("Su saldo es: ", bono)
        print(
            "Las amenidades solicitadas no pueden ser intercambiadas por otras y su cancelacion no implica la devolucion de su bono")
    else:
        print(
            "Notamos que decidio no utilizar ninguna amenidad.\nLa tienda de regalos tiene un pin Hard Rock para que lo lleve como recuerdo.")
else:
    print("Gracias por su preferencia")

