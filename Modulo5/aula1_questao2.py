import random
import math

n = int(input("Digite o número de valores aleatórios a serem gerados: "))

valores = [random.randint(0, 100) for _ in range(n)]

soma = sum(valores)

raiz_quadrada = math.sqrt(soma)

print("Os valores gerados são:", valores)
print("A soma dos valores é:", soma)
print("A raiz quadrada da soma é:", raiz_quadrada)