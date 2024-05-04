ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")

testar_anos = [1900, 2000, 2016, 2017]

for ano in testar_anos:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        resultado = "Bissexto"
    else:
        resultado = "Não Bissexto"
    print(f"O ano {ano} é {resultado}.")