word = input("Dame el string: ")
contPalabras = 0
separacion = True

for i in word:
    if i != " " and separacion == True:
        contPalabras += 1
        separacion = False
    elif i == " ":
        separacion = True

print("Usted tiene ", contPalabras, " palabras")


#lorenzo le hace tareas al mym