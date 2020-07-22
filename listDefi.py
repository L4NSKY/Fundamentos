lista = [-3, 2, 7, 8, 4, 2, -2, 0, -1, -9, -11, -5, 5]
entre = 0
menores = 0
mayores = 0

for i in lista:
    if i > -5 and i < 5:
        entre += 1
    elif i <= -5:
        menores += 1
    else:
        mayores += 1

print("Numeros entre: ", entre, " numenros menores: ", menores, " numeros mayores: ", mayores)