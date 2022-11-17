real = float(input('Quanto dinheiro você tem? R$'))
dolar = real / 5.48
euro = real / 5.65
ienes = real / 0.039
print('com R${:.2f} você pode comprar:\nUS${:.2f}\nЄ{:.2f}\n¥{:.2f}'.format(real, dolar, euro, ienes))