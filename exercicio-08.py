# escreva um programa que leia um valor em metros, convertido em centimetros e milimetros
# km  hm dam m dm cm mm
medida = float(input('uma distãncia em metros'))
km = medida * 100  # kilometro
hm = medida * 100 # hequitometro
dam = medida * 100  # decametro
m = medida * 100  # metro
cm = medida * 100  # centimentro
mm = medida * 1000 # melimetro



print('A medida de {}m corresponde a {}km e {}hm e {}dam e {}m e {}dm e {}mm  '.format(medida, km, hm, dam, m, cm, mm))