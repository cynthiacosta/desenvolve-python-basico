n = int(input("Digite o valor de n: "))

maior = 0

while n > 0:
    
    x = int(input("Digite um valor para x: "))

    if x > maior:
        maior = x

    n -= 1

print(f"O maior valor é: {maior}")