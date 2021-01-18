##Machine Teaching Lab 8


##1)Soma de Numeros Impares:
def soma_impar(n):
    '''Funcao que retorna a soma dos n primeiros numeros impares, onde
    n e um inteiro passado como parametro.
    int -> int'''
    soma = 0
    for i in range(1,n*2,2):
        soma = soma + i
    return soma
    
##2)Soma Fatorial:
from math import factorial
def soma_fatorial():
    '''Funcao que calcula a soma dos fatoriais dos numeros inteiros de 1 a 10.
    sem parametro de entrada -> int'''
    soma = 0
    for f in range(1,11):
        soma = soma + factorial(f)
    return soma

##3)Divisores:
def divisores(num):
    '''Funcao que conta quantos divisores o numero num,
    que e passado como entrada, tem.
    int -> int'''
    soma = 0
    
    for d in range(1,num+1):
        if num % d == 0:
            soma = soma + 1
    return soma

##4)Numeros Primos:
def primo(nip):
    '''Funcao que, dado um numero inteiro positivo,
    diz se ele é primo ou nao.
    int -> bool'''
    
    for x in range(2,nip):
        if nip % x ==0:
            return False
    else:
            return True

##5)Soma H:
def soma_h(N):
    '''Funcao que calcula e retorna o valor de H com N termos, onde N
    e dado como parametro. Retorne o resultado somente com 2 casas decimais.
    int -> float'''
    soma = 0
    for x in range(1,N+1):
        soma = soma + 1/x
    return round(soma,2)

##6)Soma Esquisita:
from math import factorial
def soma():
    '''Funcao que calcula a soma dos fatoriais  de 1 a 10.
    sem parametro de entrada -> float'''
    soma = 0
    for f in range(1,11):
        soma = f/factorial(11-f) - soma
    return round(soma,2)

##7)Lingua do P:
def lingua_p(frase):
    '''Funcao que recebe uma palavra como parametro e retorna a mesma traduzida
    para a lingua do p; isso significa inserir apos cada vogal a letra p e
    a sequencia de p mais a vogal
    str -> str'''
    vogais = 'ãaáàeéèiíoóuú'
    vogaisup = str.upper(vogais)
    palavra = ''

    for letra in frase:
        if letra in vogais:
            palavra = palavra +  letra + 'p' + letra
            
        elif letra in vogaisup:
            palavra = palavra +  letra + 'p' + letra
            
        else:
            palavra = palavra + letra
    return str.lower(palavra)
