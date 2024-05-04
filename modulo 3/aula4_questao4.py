distancia = float(input("Digite a distância da entrega em quilômetros: "))

peso = float(input("Digite o peso do pacote em quilogramas: "))

if distancia <= 100:
    custo_por_kg = 1.0
elif distancia <= 300:
    custo_por_kg = 1.5
else:
    custo_por_kg = 2.0

frete = custo_por_kg * peso

if peso > 10:
    frete += 10

print(f"O valor do frete é: R${frete:.2f}")