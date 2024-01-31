# convencao do real pra o dolar 
real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 4.97
euro = real /  5.36 
print('Com R$ {:.2f} vc pode compra US$ {:.2f}'.format(real, dolar))
print('Com R$ {:.2f} vc pode compra € {:.2f}'.format(real, euro))# pra aparece o simbolo do euro alt+0128
