def segundos(segundos):
    print("Se puede convertir a: ")
    dias = segundos // 86400
    segundos = segundos - (dias * 86400)
    horas = segundos // 3600
    segundos = segundos - (horas * 3600)
    minutos = segundos // 60
    segundos = segundos - (minutos * 60)

    print (f"dias: {dias}")
    print (f"horas: {horas}")
    print (f"minutos: {minutos}")
    print (f"segundos: {segundos}")

secs = int(input("Dame los segundos: "))
segundos(secs)