def piesToCm(pies):
    result = pies * 30.48
    return result

feet = float(input("Dame la medida en pies: "))
resultado = piesToCm(feet)

print("En cm es: ", resultado)