def compara(num1, num2):
    if num1 < num2:
        return -1
    elif num1 == num2:
        return 0
    else:
        return 1

nume1 = int(input("Dame el num1 a comparar: "))
nume2 = int(input("Dame el num2 a comparar: "))

result = compara(nume1, nume2)

print("regresa: ", result)