
kcal_total = 0.0

total_alimentos = int(input("Quantos alimentos você ingeriu?"))

for alimento in range(1, total_alimentos + 1):
    kcal_atual = float(input("Kcal da refeição {}:".format(alimento)))
    kcal_total += kcal_atual

print("Total de Kcal diárias: {}".format(kcal_total))
