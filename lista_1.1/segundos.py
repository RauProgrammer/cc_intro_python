def total_segundos(segundos):
    total_segundos = segundos % 60
    minutos = segundos // 60
    total_minutos = minutos % 60
    horas = minutos // 60
    total_horas = horas % 24
    total_dias = horas // 24

    print(total_dias, "dias,", total_horas, "horas,", total_minutos, "minutos e", total_segundos, "segundos.")

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

total_segundos(segundos)
