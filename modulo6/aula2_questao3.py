import random
from collections import Counter

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = list(set(lista1).intersection(lista2))

contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

print("lista1 -", lista1)
print("lista2 -", lista2)
print("Interseccao -", sorted(interseccao))

print("Contagem")
for elemento in sorted(interseccao):
    print(f"{elemento}: (lista1={contagem_lista1[elemento]}, lista2={contagem_lista2[elemento]})")
