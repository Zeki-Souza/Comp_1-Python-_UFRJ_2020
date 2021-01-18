##Machine Teaching Lab 7

##1)Filtra Multiplos:
def filtraMultiplos(lista,n):
    '''Função que filtra os múltiplos de um número n, recebendo como entrada
    uma lista de números e o número. Ela dever retornar uma outra lista
    contendo todos os elementos da lista original que forem divisíveis por n
    list, float -> list'''
    lista1 = ()
    i = 0
    while i < len(lista):
        if int(lista[i])%n == 0:
            lista1 = lista1 + (lista[i],)
        i = i + 1
    return list(lista1)

##2)Consoantes e Maiusculas:
def uppCons(frase):
    '''Função que recebe uma frase e retorne a mesma com todas as suas
    consoantes em maiúsculas e os demais caracteres exatamente como estavam.
    str -> str'''
    i = 0

    while i < len(frase):
        if frase[i] not in 'aeiouAEIOUãáàéèíóôú':
            frase = frase.replace(frase[i],frase[i].upper())
        i = i+ 1
    return frase

##3)Posicao da Letra:
def posLetra(texto,letra,ocorrencia):
    '''Função que recebe uma string, uma letra e um número. O número indica a
        ocorrência desejada da letra (1 para primeira ocorrência,
        2 para segunda, etc). A função deve retornar em que posição da string
        aquela ocorrência da letra está. Caso exista menos ocorrências
        da letra do que a ocorrência pedida, a função deveretornar -1.
        str, str, int -> int'''
    i = 0
    n = 0
    while i<len(texto) and n<ocorrencia:
        if texto[i] == letra:
            n = n +1
        i = i + 1
    if n < ocorrencia:
        return -1
    else:
        return i-1

##4)Repetidos:
def repetidos(listaR):
    '''Função que receba uma lista de números, e retorne o número
    de vezes ocorre uma série de números iguais.
    list -> int'''
    cont = 0
    j = 1
    while j < len(listaR):
        if listaR[j] == (listaR[j-1]):
            listaR.count(listaR[j])
            cont += 1
        j += 1
    return cont

##5)Fatorial:
def fatorial(num):
    '''função que dado um número, calcule o fatorial deste número.
    (Não usar a função factorial do módulo math).
    int -> complex'''
    fat = num
    while num > 1:
        fat = fat * (num - 1)
        num -= 1
    return fat

##6)Peça Perdida:
def faltante(pecas):
    '''Função que,dada uma lista com N − 1 inteiros numerados de 1 a N,
    descubra qual número inteiro deste intervalo está faltando.
    Entrada: O parâmetro de entrada é uma lista L de tamanho N − 1
    contendo números inteiros (não repetidos) de 1 a N.
    Saída: A função deve retornar o número inteiro x que pertence ao
    intervalo [1, N] mas que não pertence a lista de entrada L.
    list -> int'''
    list.sort(pecas)

    if pecas[0] != 1:
        return 1

    lista = list(range(pecas[0],pecas[-1]+1))
    if lista == pecas:
        return pecas[-1] + 1

    i = 0
    while i < len(lista):
        if lista[i] != pecas[i]:
            return lista[i]

        i = i+1

    else:
        return i-1
