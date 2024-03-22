'''from datetime import date
atual = date.today().year
cont = 0
for c in range (1,7+1):
    nascimento = int(input('Ano de nascimento: '))
    idade = atual - nascimento
    cont = cont + c
if idade >= 18:
        print('Esse(s) indivíduo(s) possue(m) {} anos de idade. Temos a semiose de um programa que extrai o número de {} indivíduos maior(es) de 18 anos.'.format(idade, cont))
elif idade < 18:
        print('Esse(s) indivíduo(s) possue(m) anos de idade. Temos a semiose de um programa que extrai o número de {} indivíduos menor(es) de 18 anos.'.format(idade,cont))'''

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 7+1):
    nascimento = int(input('Ano de nascimento da {}° pessoa: '.format(pess)))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))