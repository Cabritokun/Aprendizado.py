#apenas um escolhido

from random import choice
n1 = str(input('digite o primeiro nome: '))
n2 = str(input('digite o segundo nome: '))
n3 = str(input('digite o terceiro nome: '))
n4 = str(input('digite o quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('o escolhido foi :{} '.format(escolhido))

#sorteio de 4 pessoas em ordem aleatória

import random
n1 = str(input('digite o primeiro nome: '))
n2 = str(input('digite o segundo nome: '))
n3 = str(input('digite o terceiro nome: '))
n4 = str(input('digite o quarto nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a ordem de apresentação será:')
print(lista)



