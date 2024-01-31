# Dobro, Triplo, Raiz Quadrada

#n = int(input('digite um número:'))
#d = n * 2
#t = n * 3
#r = n ** (1/2)

#print('o dobro de {} vale {}.'.format(n, d))
#print('o triplo de {} vale {}. A raiz quadrada de {} é igual a {}.'.format(n, t, n, r))

# outro meio de fazer 

n = int(input('digite um número:'))
print('o dobro de {} vale {}.'.format(n, (n*2)))
#print('o triplo de {} vale {}. A raiz quadrada de {} é igual a {}.'.format(n, (n*3), n, (n**(1/2))))

# outro mexemplo usando pow pra raiz quadrada

print('o triplo de {} vale {}. A raiz quadrada de {} é igual a {}.'.format(n, (n*3), n, pow(n, (1/2))))