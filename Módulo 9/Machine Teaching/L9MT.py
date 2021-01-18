##Machine Teaching Lab 9


##1)Matriz Quadrada:
def ehquadrada(matriz):
    '''Funcao que recebe uma matriz nao-vazia e retorna se a mesma e ou nao
    uma matriz quadrada.
    list(list) -> bool'''
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True
        else:
            return False


##2)Buscando na Matriz:
def conta_numero(numero,matriz):
    '''Funcao que recebe um numero inteiro e uma matriz de inteiros e conta
    quantas vezes o tal numero aparece na matriz.
    int, list(list(int)) -> int'''
    quantidade = 0
    for linha in matriz:
        quantidade = quantidade + list.count(linha,numero)
    return quantidade
    

##3)Média na Matriz:
def media(matriz):
    '''Funcao que recebe uma matriz de inteiros, nao vazia, e retorna a media
    de todos os numeros dela.
    list(list) -> float'''
    med = 0
    for linha in matriz:
        for elemento in linha:
            med = med + elemento
        conta = med/(len(matriz)*len(matriz[0]))
    return round(conta,2)
    

##4)Melhor Volta:
def melhor_volta(resultados):
    '''Funcao que recebe uma matriz com os tempos dos corredores e retorna uma
    tupla com a melhor volta da prova, o tempo e em qual volta.
    list(list(int)) -> tuple(int)'''
    melhorV = []
    for corredor in resultados:
        list.append(melhorV,min(corredor))
    b = min(melhorV)
    a = list.index(melhorV, b)
    c = list.index(resultados[a],b)
    return (a+1,b,c+1)


##5)Busca de Funcionarios:
def busca(setor,matriz):
    '''Função que recebe uma string chamada setor, que é parte da matriz de
    strings, e retorna as sublistas que contém tal string dentro da matriz.
    list(list(str)) -> list(str)'''
    resposta = []
    for funca in matriz:
        if funca[2] == setor:
            list.append(resposta, funca[:2] + funca[3:])
    if resposta != []:
        return resposta
    return []


##6)Algoritimos de Busca:
def sorted(lista):
    '''Funcao que recebe uma lista como entrada e retorna a mesma estando
    ordenada em ordem crescente.
    list -> list'''
    i =0
    while i < len(lista) -1:
        if lista[i+1] < lista[i]:
            m = lista[i+1]
            lista[i+1] = lista[i]
            lista[i] = m
            i = -1
        i = i+1
    return lista
