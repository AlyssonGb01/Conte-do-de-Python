cd = int(input("Código de empregado: "))
nasc = int(input("Ano de nascimento: "))
ing = int(input("Ano de ingresso na empresa: "))
idade = 2026-nasc
tempo = 2026-ing
print(f"Código: {cd}")
print(f"Idade: {idade} anos ")
print(f"Tempo de trabalho: {tempo} anos ")
if (idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25)):
    print("Requerer aposentadoria")
else:
    print("Não precisa viadin")
    print("Não precisa viadin")