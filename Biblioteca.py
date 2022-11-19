import math
num = int(input('digite um numero: '))
raiz = math.sqrt(num)
#arredondando para cima
print('a raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
