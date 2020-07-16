def fecha(dia, mes, year):
    if dia <= 0 or dia > 31:
        print("La fecha insertada no es valida")
    elif mes < 1 or mes > 12:
        print("La fecha insertada no es valida")
    elif year < 0:
        print("La fecha insertada no es valida")
    else:
        print("La fecha es valida")

dia = int(input("Dame el dia: "))
mes = int(input("Dame el mes: "))
yr = int(input("Dame el año: "))

fecha(dia, mes, yr)