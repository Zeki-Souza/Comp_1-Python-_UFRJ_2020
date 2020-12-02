##Questão 1:
##Voltamos ao desenvolvimento da aplicacao contatinhosApp.
##Nesta semana, sua tarefas e desenvolver a funcionalidade
##”quem ligou”, ou seja, dado um numero de telefone, faca uma func˜ao
##que retorne a lista com os dados do contatinho que tem aquele numero
##(ou uma lista vazia caso o numero n˜ao esteja salvo na agenda).
def quem_ligou(agenda,numero):
    '''Funcao que recebe uma agenda com iformações de contatos,
    um numero de telefone e retorna o contato correspondente a tal numero.
    list(list(str), str - > list(str)'''
    M = []
    for j in range(len(agenda)):
        if numero in agenda[j][1]:
            M.append(agenda[j])
    return M
