__author__ = 'Frederico da Silva Santos'
__date__ = '27/02/2014'
'''
Módulo random do Python
'''
from random import *

def generate_number():
    '''
    Gera número inteiro aleatório entre 1 e 1000
    '''
    return randint(1, 1001)

def generate_raffle():
    '''
    Realizando um sorteio com a função choice do módulo random
    '''
    people = [
        {'Nome':'João','idade':20, 'Email': 'joao@gmail.com'},{'Nome':'Ana','idade':35, 'Email': 'ana@gmail.com'}\
        ,{'Nome':'Pedro','idade':18, 'Email': 'pedro@gmail.com'},{'Nome':'Maria','idade':48, 'Email': 'maria@gmail.com'}
    ]
    return choice(people)

def generate_sena():
    '''
    Sorteio da Mega-Sena usando a função sample do módulo random
    '''
    nums = list(range(1,61))#Lista de números entre 1 e 60
    return sorted(sample(nums,6))#Retorna uma lista de 6 números já ordenada


if __name__ == '__main__':
    print('Inteiro aleatório: %d' % generate_number())
    print('Sorteio: %s' % generate_raffle())
    print('Mega-Sena: %s' % generate_sena())