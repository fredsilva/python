__author__ = 'Frederico da Silva Santos'
__date__ = '05/03/2014'

'''
Utilizando list comprehensions em Python
'''

from math import pow

def even_numbers():
    '''
    Gerando lista de números pares entre 1 e 50
    '''
    return [x for x in range(1,51) if x%2 == 0]

def numbers_multiple_3():
    '''
    Elevando todos os múltiplos de 3 entre 1 e 100 a 3ª potência
    '''
    return [pow(x,3) for x in range(1,101) if x%3 == 0]

if __name__ == '__main__':
    print('Números pares: %s' % even_numbers())
    print('Números elevados a potência de 3: %s' % numbers_multiple_3())
