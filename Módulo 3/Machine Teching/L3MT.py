##Machine Teaching Lab 3


##1)Positivo, Negativo ou Zero?
def PosNegZero(x):
    '''Funcao que determina se um numero inteiro x e positivo, negativo ou zero, 
        retornando uma funcao string. int - str'''
    if x > 0:
        return str(x) + ' e positivo'
    elif x < 0:
        return str(x) + ' e negativo'
    else:
        return str(x) + ' e zero'

##2)Futebol
def classificacao(cv, ce, cs, fv, fe, fs):
    '''Funcao que determina qual dos times esta melhor classificado num campeonado, tendo
        como parametros os numeros inteiros cv, ce,cs,fv,fe,fs que representam respectivamente
            o numero de vitorias, numero de empates e saldo de gols de ambos os times
                int,int,int,int,int,int - str'''
    pontosc = cv * 3 + ce
    pontosf = fv * 3 + fe
    if (pontosc > pontosf):
        return 'Cormengo'
    if (pontosf > pontosc):
        return 'Flaminthians'
    elif (pontosc == pontosf):
        if (cs > fs):
            return 'Cormengo'
        if (fs > cs):
            return 'Flaminthians'
        else:
            return 'Empate'

##Aviões de Papel
def avioes(c, p_compr, p_compet):
    '''Funcao que define se certa quantidade de papel p_compr sera suficiente
        para uma quantidade c de participantes participarem de uma competicao de
            avioes de papeis onde cada um recebera uma quantidade p_compet de papeis.
                int,int,int - str'''
    if (p_compr/c >= p_compet):
        return 'Suficiente'
    else:
        return 'Insuficiente'
