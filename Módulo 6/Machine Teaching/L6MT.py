##Machine Teaching Lab 6

##1)Altera Frase:
def altera_frase(frase,palavra,posicao):
    '''Função que recebe uma frase, uma palavra e uma posição e:
        caso a palavra já exista na frase, transforme a primeira ocorrência em
        maiúscula. Caso a palavra não exista, insira a palavra na posição dada,
        e assuma que a primeira palavra está na posição 0
        Entrada: lista(string, string, int) ; Saída: lista(string)'''

    if palavra in frase:
        frase_split = str.split(frase)
        indice_frase = frase_split.index(palavra)
        frase_split[indice_frase] = str.upper(palavra)
        return str.join(' ', frase_split)

    elif palavra not in frase:
        frase3 = str.split(frase)
        list.insert(frase3,posicao,palavra)
        frase4 = str.join(' ',frase3)
        return frase4

##2)Faltas no ampeonato:
def faltas(time):
    '''Função que recebe uma lista, com dois times e seus respectivos números de falta,
        e retorna o total de faltas realizadas no campeonato.
        Entrada: lista(sting, string, int, int) ; Saída: int'''
    p1 = time[0][2][0] + time[0][2][1]
    p2 = time[1][2][0] + time[1][2][1]
    p3 = time[2][2][0] + time[2][2][1]
    return p1 + p2 + p3

##3)Insere Ordenado:
def insere(lista_numero,n):
    '''Função que, dada uma lista ordeanada(crescente) de números inteiros e
        um número inteiro n, inclua n na posição correta de tal maneira que
        a lista continue ordenada.
        Entrada: lista(int, int) ; Saída: lista(int)'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero

##4)Maiores:
def maiores(lista_inteiros,n):
    '''Função que recebe uma lista de números inteiros, um número inteiro n
        e retorna uma outra lista com todos os números da lista original que
        são maiores que n.'''
    list.insert(lista_inteiros,0,n)
    list.sort(lista_inteiros,reverse=True)
    x = list.index(lista_inteiros,n,0)
    del lista_inteiros[x::]
    

    return lista_inteiros[::-1]

##5)Acima da Média:
def maiores(lista_inteiros,n):
    '''Função que recebe uma lista de números inteiros, um número inteiro n
        e retorna uma outra lista com todos os números da lista original que
        são maiores que n.'''
    list.insert(lista_inteiros,0,n)
    list.sort(lista_inteiros,reverse=True)
    x = list.index(lista_inteiros,n,0)
    del lista_inteiros[x::]
    
    return lista_inteiros[::-1]

def media(notas):
    '''Função que, dada uma lista com as notas de alunos de uma turma, retorna
        a média da turma e uma lista ordenada com as notas que ficaram acima
        da média.
        Entrada: list(int) ; Saída: list(int)'''
    media_notas = sum(notas)/len(notas)
    maiores_notas = maiores(notas,media_notas)

    return media_notas, maiores_notas

##6)Ordenada:
def eh_ordenada(lista):
    '''Função que, dada uma lista contendo uma quantidade de valores numéricos,
        retorne se a lista está ordenada em ordem crescente, decrescente ou
        não odernada. A retorno da função deve ser uma Tupla onde o primeiro
        elemento é True, caso a lista esteja ordenada e False caso o contrário.
        O segundo elemento deve ser uma string "crescente", "decrescente" ou
        "desordenada", indicando como a lista encontra-se.
        Entrada: lista(int) ; Return: tupla(bool, str)'''
    lista2 = lista[:]
    lista.sort( )
    
    if lista2 == lista:
        return True, "crescente"

    elif lista2 == lista[::-1]:
        return True, "decrescente"

    else:
        return False, "desordenada"
