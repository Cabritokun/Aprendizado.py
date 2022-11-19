#importação de matemática
import math
  num = int(input('digite um numero: '))
  raiz = math.sqrt(num)
#arredondando para cima
print('a raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

#importação de número aleatório
import random
  num = random.randint(1, 10)
print('Seu numero aleatorio é {}'.format(num))

#importação de emoji
import emoji
print(emoji.emojize("Olá, mundo :mushroom:"))
