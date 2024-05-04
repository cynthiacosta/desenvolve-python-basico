avaliacao = int(input("Insira a avaliação do filme (1 a 5): "))

if avaliacao == 5:
    mensagem = "Excelente!"
elif avaliacao == 4:
    mensagem = "Muito Bom!"
elif avaliacao == 3:
    mensagem = "Bom!"
elif avaliacao == 2:
    mensagem = "Regular."
elif avaliacao == 1:
    mensagem = "Ruim."
else:
    mensagem = "Avaliação inválida. Por favor, insira um número entre 1 e 5."

print(mensagem)