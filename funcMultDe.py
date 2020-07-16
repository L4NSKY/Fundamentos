def multiploDe(comprobar, divisor):
    if (comprobar % divisor) == 0:
        return True
    else:
        return False

num1=int(input("Ingrese el valor 1: "))
num2=int(input("Ingrese el valor 2: "))

result = multiploDe(num1, num2)

print("El numero es multiplo: ", result)