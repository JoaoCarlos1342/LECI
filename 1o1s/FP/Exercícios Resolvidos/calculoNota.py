CTP = float(input("Qual a nota da Componente Téorica Prática? "))
CP = float(input("Qual a nota da Componente Prática"))
ctp = CTP * 0.3
cp = CP * 0.7
nota_final = ctp + cp
ATPR = 0.0
APR = 0.0

if CTP < 6.5 or CP < 6.5:
    print("66")
elif nota_final < 9.5:
    print("66")
else:
    print(nota_final)
    exit(1)

ATPR = float(input("Qual a nota de recurso teórico prático"))
APR = float(input("Qual a nota de recurso prático"))
atpr = ATPR * 0.3
apr = APR * 0.7
nota_final_recurso = atpr + apr

if ATPR < 6.5 or APR < 6.5:
    print("66")
elif nota_final_recurso < 9.5:
    print("66")
else:
    print(nota_final_recurso)