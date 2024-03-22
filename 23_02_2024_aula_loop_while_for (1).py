# -*- coding: utf-8 -*-
"""23_02_2024_aula_loop_while_for

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gnx__d1bu_J_fChNoBbkM7LKeibEPxpn

1.0 Solicitar um número inteiro positivo N ao usuário. Imprimir os números de N a 1. Realizar o exercício usando loops for e wgile
"""

T = int(input('Entre com número inteiro maior que 1: '))
#FOR
print('For: ')
for t in range(T):
  print(f'{T-t}', end =' ' )
print('\n')


#WHILE
i = 0
print('While: ')
while i < T:
  print(f'{T-i}', end =' ')
  i += 1

"""2.0 Solicitar um número inteiro positivo N ao usuário. Imprimir os números de N a 1 trocando o sinal dos números. Realizar o exercício usando loops for e while. Exemplo para N igual a 5:

```

```


"""

T = int(input('Entre com número inteiro maior que 1: '))
#FOR
print('For: ')
for t in range(T):
  print(f'{(-1) * (T-t)}', end =' ' )
print('\n')

#WHILE
i = 0
print('While: ')
while i < T:
  print(f'{(-1) * (T-i)}', end =' ')
  i += 1

"""3.0 Solicitar um número inteiro positivo N ao usuário. Imprimir os números de N a 1 alternando o sinal dos números. Realizar o exercício usando loops for e while. Exemplo para N igual a 5:

"""

N = int(input('Digite o limite: '))
mult = -1
fat = 1
for n in range (N):
  print(fat * (N-n), end = ' ')
  fat = fat * mult



"""4.0 Solicitar um número inteiro positivo N ao usuário e imprimir i² para 0 < i < N. Por exemplo, para N=5, serão impressos:

"""

N = int(input('Entre com número inteiro maior que 1 (N>0): '))
#FOR
print('For')
for i in range(0, N):
  print(f'{i*i}')
print('\n')
#While
print('While: ')
i = 0
print(f'   i  i*i  i**3')
while i < N:
  print(f'{i:4d} {i*i:4d} {i**3:4d} ')
  i += 1

"""5.0 Solicitar uma palavra ao usuário e dizer se a palavra é palíndromo, isto é, pode ser lida igualmente da esquerda para a direita e vice-versa. Exemplos de palavras que são palíndromos: ovo, radar, mirim, arara, reviver"""

palavra = str(input('Digite uma palavra: ')).strip().upper()
palavra_split = palavra.split()
palavra_join = ''.join(palavra)
palavra_inverso = ''
for letra in range(len(palavra_join) -1, -1, -1):
  palavra_inverso = palavra_inverso + palavra_join[letra]
print(f'O inverso de {palavra_join} é {palavra_inverso}.')
if palavra_inverso == palavra_join:
  print('Temos um palíndromo!')
else:
  print('A palavra digitada não é um palíndromo.')

"""6.0 Fazer um programa que solicita um número inteiro positivo N ao usuário e imprime o seguinte padrão na tela."""

M = 5
N = 4

for m in range(M):
  for n in range(N):
    print(f'{m:2d}')