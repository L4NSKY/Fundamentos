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

#Def reto 3
def empiezan_Con(listaStrings, letra):
    contadorLetra = 0

    for i in range(len(listaStrings)):
        word = listaStrings[i]
        if word[0] == letra:
            contadorLetra += 1
    return contadorLetra

#Def reto 4
def duplica(listaInts):
    dobles = []
    for i in listaInts:
        dobles.append(i*2)
    return dobles

#Def reto 5
def locura(palabra):
    newPalabra = ""
    for i in palabra:
        if i == "e":
            newPalabra += '3'
        elif i == 'o':
            newPalabra += 'h'
        elif i == "a":
            newPalabra += '4'
        else:
            newPalabra += i
    return newPalabra

#Def reto 6
def vocales_Mayusculas(aCambiar):
    newWord = ""
    for i in aCambiar:
        if i == 'a':
            newWord += 'A'
        elif i == 'e':
            newWord += 'E'
        elif i == 'i':
            newWord += 'I'
        elif i == 'o':
            newWord += 'O'
        elif i == 'u':
            newWord += 'U'
        else:
            newWord += i
    return newWord

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
        listaPalabras = []
        cantidadPalabras = int(input("Dime cuantas palabras quieres ingresar: "))
        letraContar = input("Dame la letra que quieres contar al inicio de las palabras: ")

        for i in range(cantidadPalabras):
            listaPalabras.append(input("Dame la palabra: "))
        aparece = empiezan_Con(listaPalabras, letraContar)
        print("La cantidad de palabras que empiezan con ", letraContar, " son: ", aparece)

    elif opcion == 4:
        listaInts = []
        cantidadInts = int(input("¿Cuántos enteros vas a ingresar?"))
        for i in range(cantidadInts):
            listaInts.append(int(input("Dame un entero: ")))
        duplicados = duplica(listaInts)
        print(duplicados)
    elif opcion == 5:
        palabra = input("Dame una palabra: ")
        newPalabra = locura(palabra)
        print(newPalabra)
    elif opcion == 6:
        word = input("Dame la palabra que quieres hacer sus vocales mayusculas")
        print(vocales_Mayusculas(word))