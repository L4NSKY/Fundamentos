from math import pi

def volumenEsfera(radio):
    resultado = (4/3)*pi*(radio**3)
    return resultado

rad = float(input("Dame el radio: "))
result = volumenEsfera(rad)

print("El volumen es: ", result)