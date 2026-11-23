mokg = float(input(" Quantos kg de morango você comprou: "))
makg = float(input(" Quantos kg de maçã você comprou: "))
if (mokg <= 5):
    valormo = mokg*2.50
else:
    valormo = mokg*2.20
if (makg <= 5):
    valorma = makg*1.80
else:
    valorma = makg*1.50
total = valormo+valorma 
if (mokg+makg > 8 or total > 25):
    vf = total*0.90
print(f"Você recebeu um desconto de 10 por cento, o valor a ser pago é {vf}")