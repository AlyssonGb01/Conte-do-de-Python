def somaAte(limite):
    soma = 0
    for numero in range(1, limite+1):
        soma = soma + numero

    return soma

print(somaAte(4))

print(somaAte(1000))