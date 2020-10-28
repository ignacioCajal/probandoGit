
#calcular el porcentaje de tiempo que lleva viva una persona segun su edad
def calculadorEdadPorcentual():
    edad = int(input("ingrese edad: "))
    promedioDeVida = int(input("Promedio de años de vida: "))

    calculo = (edad/promedioDeVida) * 100
    redondeo = round(calculo)
    print(f"{redondeo}% de tiempo vivo segun la esperanza de vida de tu pais")

calculadorEdadPorcentual()

def calculadorDiasDeVida():

    minutos = 60 #segundos
    horas = 60 #minutos
    dias = 24 #horas
    semanas =  7 #dias
    meses = 31 #dias
    año = 365 #dias

    #calculo =
    