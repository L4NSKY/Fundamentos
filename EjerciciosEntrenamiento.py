opcion = 0


# Capturas 1
def captura():
    lista = []
    num = int(input("Cuantos elementos me daras en la lista: "))
    for i in range(num):
        valor = int(input("Dame un numero:" ))
        lista.append(valor)
    return lista

#Captura 2
def capturaTextos():
    listaTextos = []
    num = int(input("Cuantos palabras me daras en la lista: "))
    for i in range(num):
        valor = input("Dame una palabra:")
        listaTextos.append(valor)
    return listaTextos

#Def reto 1
def mayoresN(lista, n):
    counter = 0
    for i in lista:
        if i > n:
            counter += 1
            print(i)
    return counter

#Def reto 2
def con_N_letras(lista, n):
    counter = 0
    for palabra in lista:
        if len(palabra)>=n:
            counter+=1
    return counter

while opcion != 11:
    print("\nMENU FUNCIONES\nIngrese el numero de la opcione que desea: ")
    print("1.Elementos en una lista mayores a N\n2.N letras o mas en un string\n3.\n4.\n5.\n11.Salir")
    opcion = int(input("Seleccione una ocpion: "))

    if opcion == 1:
        listanueva = captura()
        print(listanueva)
        num = int(input("Dame un numero de la lista para ver cuales son mayores a el: "))
        mayor = mayoresN(listanueva,num)
        print("En la lista hay mayor", mayor, "mayores a ", num,)

    elif opcion == 2:
        listaString = capturaTextos()
        print(listaString)
        num = int(input("Cuantas letras quieres que revise que tiene cada palabra: "))
        cuantas = con_N_letras(listaString, num)
        print("En la lista dada hay", cuantas, "palabras que tienen", num, "o mas letras")

    elif opcion == 3:


