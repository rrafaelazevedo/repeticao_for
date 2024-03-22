# -*- coding: utf-8 -*-
"""Aula_15_02_2024_For

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Z8Rxb0ufGjOW9PCgvU8iAKbj6LSAxVN
"""

#ex01_exemplo_for
maior_n = float()

for i in range(5):
  n = float(input(f'Digíte o {i+1}º numero: '))
  if n > maior_n:
    maior_n = n
  print(f'O maior número digítado é: {maior_n}')

#ex02_exemplo_for
for n in range(1000, 2001):
  if n % 11 == 2:
    print(n)

#ex03_exemplo_for
n = int(input('Digíte um número pra calcular a tabuada: '))

print(f'Tabuada de {n}: ')
for m in range(1, 10+1):
  r = n * m
  print(f'{n} x {m} = {r}')

#ex04_exemplo_for
for i in range(1, 20+1):
  print(i)
print(list(range(1, 20+1)))

#ex_01
maior_n = float()

for i in range(5):
  n = float(input(f'Digíte o {i+1}º numero: '))
  if n > maior_n:
    maior_n = n
  print(f'O maior número digítado é: {maior_n}')

#ex_02
for n in range(1000, 2001):
  if n % 11 == 2:
    print(n)

#ex_03
soma = float()
for i in range(1, 6):
  n = float(input('Digíte um número: '))
  soma += n
  media = soma/i
print(f'A soma é {soma} e a média é {media}')

#ex_04
n = int(input('Digíte um número pra calcular a tabuada: '))

print(f'Tabuada de {n}: ')
for m in range(1, 10+1):
  r = n * m
  print(f'{n} x {m} = {r}')

#ex_05
for n in range(1, 10+1):
  print(f'Tabuada do número {n}: ')
  for m in range(1, 10+1):
    r = m * n
    print(f'{m} x {n} = {r}')

#ex_06
for i in range(1, 20+1):
  print(i)
print(list(range(1, 20+1)))

#ex_07
for c in range(1, 51):
  if c % 2 == 1:
    n_impar = c
    print(c)

#ex_08
n1 = int(input('Digite o primero número do range: '))
n2 = int(input('Digite o segundo número: '))
print(f'Os números compreendidos no intervalo ]{n1}, {n2}[ são: ')
for m in range(n1+1, n2):
  print(m, end=" ")
print()
print(f'Os números compreendidos no intervalo [{n1}, {n2}] são: ')
for m in range(n1, n2+1):
  print(m, end=" ")
print()

#ex_09
c = float()
soma = float()
for c in range(0, 5):
  faturamento_a = float(input(f'Digite o valor da compra do {c+1}º cliente: '))
  soma += faturamento_a
if soma > 54000:
  print('Faturamento superado')
else:
  print('Faturamento não superado')

#ex_10
np = int()
ni = int()
for i in range(0, 10):
  n = int(input(f'Digite o {i+1}º número: '))
  if i % 2 == 0:
    np += 1
  else:
    ni += 1
print(f'A quantidade de números pares (np) inseridos são: {np}, e a quantidade números ímpares (ni) são: {ni}.')

#ex11
salario_inicial = float(1000.00)

p = (salario_inicial * 0.015)
salario_ajustado =  p + salario_inicial

for i in range(1996, 2025):
  p *= 2
  salario_ajustado = salario_ajustado + p
  print(f'O salario atual em {i} baseado no salario inicial de R${salario_inicial:.2f} é de R${salario_ajustado:.2f} unidades monetárias.')

salario_inicial = float(input('Salário inícial do colaborador em unidades monetárias (R$): '))

p = (salario_inicial * 0.015)
salario_ajustado =  p + salario_inicial

for i in range(1997, 2025):
  p *= 2
  salario_ajustado = salario_ajustado + 2*p
print(f'O salario atual baseado no salario inicial de R${salario_inicial:.2f} é de R${salario_ajustado:.2f} unidades monetárias.')

#ex12_for
for i in range(999):
  nota = int(input('Digite uma nota entre o e 10: '))
  if nota >= 0 and nota <= 10:
    break
  else:
    print(f'Valor inválido')


#ex12_while
n = -1
while n == -1:
  n = float(input('Digite uma nota entre [0, 10]: '))
  if n >= 0 and n <=10:
    print(f'A nota inserida é {n:.2f}.')
  else:
    print('Nota inválida! Digite um valor entre [0, 10]: ')
    n = -1

"""Exercicio 13 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontror os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

"""

#ex_13
n = int(input('Digíte um número inteiro: '))
for i in range(1, n):