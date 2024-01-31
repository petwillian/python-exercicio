a = input('Digite Algo:')
#print('o tipo primitivo desse valor é', type(a)) #tipo primitivo input sem defini sempre e str
#print('só tem espaços?', a.isspace())# a.isspace significa sem te espaço e um booliano
#print('É um número?', a.isnumeric())# a.isnumeric e pra sabe se tem numero no codigo booliano
#print('É alfabético?', a.isalpha())# a.isalpha se tem numero alfabetico no codigo  booliano 
#print('É alfanumérico ', a.isalnum()) # a.isalnum pra sabe se ele e alfanumerico booliano
#print('Esta em maiúsculas', a.isupper()) #a.isupper pra saber se esta em maiusculo
#print('Esta em minúcuslas', a.islower()) # a. islower pra saber se esta em minuscula
#print('Esta capitalizada?', a.istitle()) # a.istitle se tem algunha letra em maiscular

print('ele e minuscula ou maiscular {} e {} !'.format(a.isupper(), a.islower()))

