numeros = []
print("Digite pelo menos 4 números inteiros. Digite 'sair' para finalizar a entrada.")

while len(numeros) < 4 or entrada != 'sair':
    entrada = input("Digite um número ou 'sair': ")
    if entrada.isdigit():
        numeros.append(int(entrada))
    elif entrada == 'sair' and len(numeros) >= 4:
        break
    elif entrada != 'sair':
        print("Por favor, digite um número inteiro ou 'sair'.")

print("Lista original:", numeros)

print("Três primeiros elementos:", numeros[:3])

print("Dois últimos elementos:", numeros[-2:])

print("Lista invertida:", numeros[::-1])

print("Elementos de índice par:", numeros[::2])

print("Elementos de índice ímpar:", numeros[1::2])
