N = int(input("Digite o número de respondentes: "))

soma_idades = 0

for _ in range(N):
    idade = int(input("Digite a idade do respondente: "))
    soma_idades += idade

media_idades = soma_idades / N

print(f"A média das idades é: {media_idades:.2f}")