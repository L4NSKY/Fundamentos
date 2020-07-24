"""Programa que recibe dos cadenas del usuario y nos dice cuál de las dos tiene más
vocales.
"""

string1 = input("Dame una oracion para contar sus vocales: ")
string2 = input("Dame otra oracion para contar sus vocales: ")

vocales1 = ([string1.count(x) for x in "aeiou"])
vocales2 = ([string2.count(x) for x in "aeiou"])

if vocales1 > vocales2:
    print("La palabra con mas vocales es ",string1,)
else:
    print("La pabara con mas vocales es ",string2,)

