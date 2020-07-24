oracion = input("Dame una frase celebre para separarla: ")

contador = 0
lista = oracion.split()
palabras = len(lista)

print("Su oracion esta compuesta por: ",palabras,"palabras")
modificada = oracion.replace("t","7")
modificada = oracion.replace("i","1")
modificada = oracion.replace("a","*")
modificada = oracion.replace("e","3")

print (modificada)
for i in (lista):
    if len(i)>5:
        contador +=1

print("Tu programa tiene ",contador,"palabras con mas de 5 letras")
