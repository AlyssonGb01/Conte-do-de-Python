def compra(dinheiro, custo):
  if dinheiro >= custo:
    return "Sua compra foi bem sucedida!"
  else:
    falta = custo - dinheiro
    return f"Saldo insuficiente. Faltam R$ {falta:.2f} para completar."

meu_dinheiro = float(input("Quanto você tem em dinheiro? "))
custo_lanche = float(input("Qual o custo da compra? "))

mensagem = compra(meu_dinheiro, custo_lanche)
print(mensagem)