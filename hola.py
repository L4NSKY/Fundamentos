"""
Mini proyecto
Dimas Maximiliano A01748296
Entrada: Opciones del menu, noches a quedarse, entrada del numero a adivinar
Proceso: Verificar el saldo del huesped en caso de que sea candidato a bono, ofrecerle las amenidades y calcular sus gastos
Salida: Mensajes de los menus
"""



#Importo las librerias
from random import randint


print("Bienvenido a Hard Rock Nuevo Vallarta")
print("-------------------------------------")
noches = int(input("¿Cuántas noches se hospedará en Hard Rock Nuevo Vallarta?\n"))

#Inicializo las variables que uso a lo largo de el codigo
bono = 0
opcion = 0
juegojugado = 0

contKayak = 0
contBanana = 0
contMasaje = 0
contVapor = 0

#Si las noches son menores a 0 el programa pide una entrada valida, si las noches son mayores o iguales a tres el programa da el bono y si las noches son mayores a 0 y menores a 3 el programa no da el bono.
if noches <= 0:
    print("No se está registrando para ninguna noche.")

elif noches >= 3:
    bono = 1450
    print("\nUsted aplica para un bono de 1450 dlls para ser utilizado en actividades del hotel")

#En esta parte se inicia el menu con el bono
    while opcion != 4:
        print("***********************************************")
        print("Hard Rock Nuevo Vallarta - Menu de amenidades:")
        print("----------------------------------------------")
        print("CREDITO: ", bono)
        print("----------------------------------------------")
        print("1) Paseos\n2) Spa\n3) Juego en linea\n4) SALIR")
        opcion = int(input("\nIngrese el numero de la opción que desea:\n"))

#Aqui estan las  sub opciones del menu, junto con las restas a su bono y las elecciones del huesped
        if opcion == 1:
            print("\nElija de los siguientes paseos:\n1.Paseo en Kayak - $500\n2.Paseo en banana - $250")
            opcion = int(input("\nIngrese su elección: "))
            if opcion == 1 and bono >= 500:
                print("\nDisfrute del paseo")
                bono = bono - 500
                contKayak += 1
            elif opcion == 2 and bono >= 250:
                print("\nDisfrute del paseo")
                bono = bono - 250
                contBanana += 1
            elif (opcion == 1 and bono < 500) or (opcion == 2 and bono < 250):
                print("\nSu saldo no es el suficiente, pruebe eligiendo una actividad de menor costo.")

        elif opcion == 2:
            print("\nElija uno de los siguientes servicios:\n1.Masajes - $600\n2.Vapor - $300")
            opcion = int(input())
            if opcion == 1 and bono >= 600:
                print("\nDisfrute del masaje")
                bono = bono - 600
                contMasaje += 1
            elif opcion == 2 and bono >= 300:
                print("\nDisfrute del vapor")
                bono = bono - 300
                contVapor += 1
            elif (opcion == 1 and bono < 600) or (opcion == 2 and bono < 300):
                print("\nSu saldo no es el suficiente, pruebe eligiendo una actividad de menor costo")

#Aqui es donde se inicia el juego de la adivinar el numero.
#El proceso implica que despues de jugarse una vez la opcion se bloquee para el usuario.
        elif opcion == 3 and juegojugado < 1:
            numeroRandom = randint(0, 100)
            contador = 8
            ganador = False

            print("--------------------------------------------------------------")
            print("BIENVENIDO AL ADIVINADOR 3000\nEscoge un numero entre 0 y 100")
            print("--------------------------------------------------------------")

            while contador > 0:
                print("Le quedan", contador, " intentos")
                escogido = int(input("Ingrese un numero:\n"))
                if escogido == numeroRandom:
                    print("¡Felicidades! Gano un pase para la NOCHE CASINO, muestre este mensaje en recepción.\n")
                    print("Le tomó ", (9 - contador), " intentos")
                    contador = 0
                    ganador = True
                    juegojugado += 1
                elif escogido < numeroRandom:
                    print("El numero a adivinar es mayor")
                elif escogido > numeroRandom:
                    print("El numero a adivinar es menor")
                contador -= 1
            if ganador == False:
                juegojugado += 1
                print("Se le agotaron los intentos. Intente de nuevo. Su numero era:", numeroRandom, "\n")
        elif opcion == 3 and juegojugado > 0:
            print("\nSolo se puede jugar una vez, por favor elija otra opción. \n")

#Esta parte se muestra despues de que el usuaario decidio cerrar el programa y muestra las amenidades que se utilizaron, si no se gasto no se muestra nada.
    if bono < 1450:
        if contKayak > 0:
            print("Usted utlizo el servicio de Paseo en kayak", contKayak, "veces con un costo total de:",contKayak * 500)
        if contBanana > 0:
            print("Usted utlizo el servicio de Paseo en banana", contBanana, "veces con un costo total de:",contBanana * 250)
        if contMasaje > 0:
            print("Usted utlizo el servicio de masaje", contMasaje, "veces con un costo total de:", contMasaje * 600)
        if contVapor > 0:
            print("Usted utlizo el servicio de vapor", contVapor, "veces con un costo total de:", contVapor * 300)
        print("Su saldo es:", bono)
        print(
            "Las amenidades solicitadas no pueden ser intercambiadas por otras y su cancelacion no implica la devolucion de su bono")
    else:
        print(
            "Notamos que decidio no utilizar ninguna amenidad.\nLa tienda de regalos tiene un pin Hard Rock para que lo lleve como recuerdo.")
else:
    print("Gracias por su preferencia")


