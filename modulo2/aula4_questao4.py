valor = int(input("Digite um valor em reais: "))

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade_notas = valor // nota
    valor %= nota
    print(f"{quantidade_notas} nota(s) de R${nota},00")