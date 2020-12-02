

##1)Faça uma função que simule um jogo de dois dados. A função deve
##contar quantos dados foram jogados até que saiam números repetidos.
##Use a função randint do módulo random. Não tem dados de entrada.

import random

def dados():
    '''Função que simula um jogo de dois dados, de modo
    que conte quantos dados foram jogados até que
    saiam números repedidos.
    Sem parâmetro de entrada -> int'''
    contador = 1

    primeiro = random.randint(1,6)
    segundo = random.randint(1,6)

    while primeiro != segundo:
        primeiro = random.randint(1,6)
        segundo = random.randint(1,6)
        contador = contador + 1

    return contador


##2)Trabalhando num app, minhas tarefas são:
##Buscar os dados de um contato salvo:
##sua funcão recebe como entrada a lista de contatos e uma string referente
##ao nome buscado, e deve retornar uma lista de contatos que tem o nome buscado.
##Mais detalhes:
##I)Como as informações de cada contatinho estão em uma lista, sua função irá
##retornar uma lista de listas, no mesmo formato que a lista contatos.
##
##II)Na lista retorno, dever˜ao constar todos os contatinhos cujo nome
##corresponde ao nome buscado (o nome buscado seja substring do nome do contato,
##desconsiderando diferenças entre letras maiu´sculas e minúsculas).
##
##III)Por exemplo, se foi buscado ’ﬁeld’, seria retornado os dados da
##”Julia Fields” e tambem do ”Fieldsnei Campos Jr”,
##caso ambos estivessem salvos no aplicativo
##
##IV)A lista de retorno não deve ter coias das informacoes de cada contatinho,
##e sim aliases (referencias) para as informacoes dos contatinhos na
##lista de contatos original. Ou seja, se identiﬁquei que o elemento
##indice 1 da lista de contatos original (os dados da ”Julia Fields”,
##por exemplo) deve fazer parte da lista de retorno,
##vou acrescentar na lista de retorno contatos[1], e n˜ao contatos[1][:]
##
##V)Se o nome buscado não corresponder a nenhum contatinho,
##deve ser retornada uma lista vazia.

def contatinhosApp(dados,busca):
    '''Função que recebe os contatos de uma pessoa em
    uma lista, e retorna uma outra lista com
    contatos que tem o nome buscado a partir do
    parâmetro busca.
    list -> list'''
    contatos = []
    i = 0
    while i < len(list(dados)):
        if busca in dados[i][0] or busca in str.lower(dados[i][0])or busca in str.upper(dados[i][0]):
            contatos.append(dados[i])
        i = i+1
    return contatos

        
    
    

