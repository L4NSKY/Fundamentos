def divPalabras(word, num):
    counter = 0
    newWord = ""

    for i in range(len(word)):
        if counter == num:
            newWord += "-"
            counter = 0
        newWord += word[i]
        counter += 1
    return newWord

palabra = input("Dame la palabra: ")
numero = int(input("Dame el numero: "))

print(divPalabras(palabra, numero))