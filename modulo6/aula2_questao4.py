def receber_lista(n):
    return [int(input(f"Digite o {i+1}º elemento: ")) for i in range(n)]

n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = receber_lista(n1)

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = receber_lista(n2)

lista_intercalada = []
min_length = min(len(lista1), len(lista2))

for i in range(min_length):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

lista_intercalada.extend(lista1[min_length:])
lista_intercalada.extend(lista2[min_length:])

print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))
