numero1 = int(input("Digite o primeiro número: "))

numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2

if soma % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"

print(f"A soma de {numero1} e {numero2} é {resultado}.")