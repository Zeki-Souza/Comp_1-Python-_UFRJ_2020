
##Questão 1: Considerando a série:

##a)
def soma_serie(n):
    '''Funcao que dado n, calcula a soma da série até o termo n
        int -> float'''
    soma = 0
    for i in range(n+1):
        soma = soma + ((-1)**i)/(2*i+1)
    return soma
##b)
import math
def serie_erro():
    '''Função que calcula a soma da serie com um erro inferior
    a 0,01.A função tambem deve retornar uma tupla com os dois
    valores calculados.
    Sem parâmetro de entrada -> tuple'''
    a = 0
    v = 0
    while abs(soma_serie(a) -(math.pi/4)) >= 0.01:
        a = a + 1
        v = v + 1
    return (soma_serie(a), v)
##Questão 2: Desenvolva uma nova vers˜ao da func˜ao desenvolvida para resolver
##a questão 2 do Laboratório 7, usando dessa vez comandos for
## para implementar as estruturas de repeticao sempre que possivel
def contatinhosApp(dados,busca):
    '''Função que recebe os contatos de uma pessoa em uma lista, e retorna
    uma outra lista com contatos que tem o nome buscado a partir do parâmetro
    busca. list -> list'''
    contatos = []
    for i in range(0,(len(dados))):
        if busca in dados[i][0] or busca in str.lower(dados[i][0])or busca in str.upper(dados[i][0]):
            contatos.append(dados[i])
        i = i+1
    return contatos
