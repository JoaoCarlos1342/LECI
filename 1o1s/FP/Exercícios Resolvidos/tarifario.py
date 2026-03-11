tarifario_base = 0.12
tarifario_segundo = 0.06
tempo = int(input("Quanto tempo demorou a chamada? "))
custo_total = 0.0

if tempo > 60:
    custo_total = tarifario_base + tarifario_segundo * (tempo - 60)
    print("O custo total da chamada é {}".format(custo_total))
else:
    print("O custo total da chamada é {}".format(tarifario_base))