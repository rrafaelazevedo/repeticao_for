n = int(input('Digite o número que deseja obter a tabuada: '))
print('A tabuada do número {} é dada pela expressão multiplicativa dos coeficientes (n * m). Para n = {} e m = [1, 10]:'.format(n,n))
for m in range(1, 10+1):
        print('{} * {} = {}'.format(n, m, n*m))



