objeto = str(input('Qual objeto voce quer saber a medida? '))
medida = float(input('digite a medida em metros: '))
cm = medida * 100
mm = medida * 1000
print('o seu(a) {} de {:.0f}m \ntem {:.0f}cm \n {:.0f}mm'.format(objeto, medida, cm, mm))
