genero = input("Informe seu gênero (M ou F): ").upper()

idade = int(input("Informe sua idade: "))

tempo_servico = int(input("Informe seu tempo de serviço em anos: "))

if genero == "F":
    regra_A = idade > 60
    regra_B = tempo_servico >= 30
    regra_C = idade >= 60 and tempo_servico >= 25
elif genero == "M":
    regra_A = idade > 65
    regra_B = tempo_servico >= 30
    regra_C = idade >= 65 and tempo_servico >= 25
else:
    regra_A = regra_B = regra_C = False

pode_se_aposentar = regra_A or regra_B or regra_C

print(pode_se_aposentar)