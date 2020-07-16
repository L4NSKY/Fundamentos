def cuadratica(a, b, c, x):
    result = (a*(x**2))+(b*x)+c
    return result

x = int(input("Dame el valor de X "))
a = int(input("Dame el valor del coeficiente a "))
b = int(input("Dame el valor del coeficiente b "))
c = int(input("Dame el valor del coeficiente c "))

resCuad = cuadratica(a,b,c,x)
print("El resultado de tu cuadratica es: ", resCuad)