larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
área = larg * alt
print('Sua parede tem dimensão de {}x{} e a sua área é de {}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede é necessário {}l de tinta'.format(tinta))