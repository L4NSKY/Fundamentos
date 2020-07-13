km = int(input("¿Hasta cuantos kilometros quieres convertir? "))

print("Kms\tEquivalente en millas")
for i in range(1, km + 1, 1):
    print(i, "\t", i * 0.62)