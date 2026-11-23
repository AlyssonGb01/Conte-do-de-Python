def compra(dinheiro, custo):
    dinheiro = float(input("Quanto você tem em dinheiro?"))
    custo = float(input("Qual o custo da compra?"))
    vcplm = custo-dinheiro
    if dinheiro >= custo: 
        return("Sua compra foi bem sucedida! ")
    else:
        return("Saldo insuficiente. ")
