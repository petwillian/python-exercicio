n = int(input('Digite um numero:'))
a = n - 1
s = n + 1
#print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s)) # primeira forma de fazer
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1))) # segunda forma de fazer pra economiza memoria
# Antecessor e Sucessor