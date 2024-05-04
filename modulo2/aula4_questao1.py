# Lê o comprimento do terreno em metros
comprimento = int(input("Informe o comprimento do terreno em metros: "))

# Lê a largura do terreno em metros
largura = int(input("Informe a largura do terreno em metros: "))

# Lê o preço do metro quadrado do terreno em ponto flutuante
preco_m2 = float(input("Informe o preço do metro quadrado do terreno: "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Imprime a área e o preço total do terreno, formatando o preço
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")