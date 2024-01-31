# medi a largura e altura de uma parede 
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print('Sua parede tem a dimesão de {}x{} e sua area e de {}m2'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, vc precisará de {} LT de tinta.'.format(tinta))