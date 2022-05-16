a=float(input('Qual a altura da sua parede? '))
l=float(input('Qual a largura da sua parede? '))
area= a*l
tinta= area/2
print(f'Essa parede tem {area:.1f}m²,', end=' ')
print(f'para pinta-la é necessário {tinta:.1f} latas de tinta.')