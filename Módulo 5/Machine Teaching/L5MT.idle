##Machine Teaching Lab 5


##1)Quantidade de palavras
def quant_palavras(frase):
    """Função que, dada uma frase, retorna o numero de palavras da frase,
        considerando que a mesma pode ter espaços no início e no final.
        Entrada: list (str) ; Saida: int"""
    spl = str.split(frase)
    return  len(spl)

##2)Conta Frases
def conta_frases(frases):
    '''Função que conta o numeo de frases que aparecem em um texto, onde cada
        frase é terminada com um ponto final, de exclação, interrogação ou
        retircências.
        Entrada: lista (str) ; Saída: int'''
    '.' != '...'
    ponto = str.count(frases,'.',0)
    exclamacao = str.count(frases,'!',0)
    duvida = str.count(frases, '?', 0)
    reticencias = str.count(frases, '...',0)
    
    return ponto + exclamacao + duvida + -2* reticencias

##3)Intercalando Listas
def intercala(lista1, lista2):
    """Função que, dado duas lista L1 e L2  de tamanho 3,
        gera uma terceira lista L3 que é formada pela
        intercalação dos elementos das listas L1 e L2.
        Entrada: list (int), list (int) ; Saída: list (int)"""
    A = lista1[0] , lista2[0] ,lista1[1]
    B = lista2[1] , lista1[2] , lista2[2]
    
    return list(A) + list(B)

##4)Retira Pontuação
def retira_pontuacao(frase3):
    '''Função que, dada uma frase, retorna uma outra frase onde todos os
        caracteres de pontuação(travessão, vírgula, dois pontos, ponto e virgula e
        ponto final) tenham sido substituídos por espaço.
        Entrada: list(str) ; Saída: list(str)'''
    a = str.replace(frase3,'.',' ')
    b = str.replace(a,",",' ')
    c = str.replace(b,';',' ')
    d = str.replace(c,':',' ')
    e = str.replace(d,"-",' ')
    f = str.replace(e,'!',' ')
    g = str.replace(f,'?',' ')
    return g

##5)De trás pra frente
def pontuacao(frase3):
    '''Função que, dada uma frase, retorna uma outra frase onde todos os
        caracteres de pontuação(travessão, vírgula, dois pontos, ponto e virgula e
        ponto final) tenham sido substituídos por espaço.
        Entrada: list(str) ; Saída: list(str)'''
    a = str.replace(frase3,'.','')
    b = str.replace(a,",",'')
    c = str.replace(b,';','')
    d = str.replace(c,':','')
    e = str.replace(d,"-",' ')
    f = str.replace(e,'!','')
    g = str.replace(f,'?','')
    return g

def inverte(frase4):
    '''Função que retorne uma frase ao contrário mas sem letras maiúsculas e sem
        pontuação. Entrada: list(str) ; Saída: list(str)'''
    p1= pontuacao(frase4)
    p2 = str.lower(p1)
    p3 = str.split(p2, " ")
    p4 = p3[::-1]
    p5 = str.join(" ",p4)
    return p5

##6)Pirâmede de Números
def piramide_num(n1,n2):
    '''Função que recebe dois números inteiros e retorna uma sequência onde o
        primeiro número é o primeiro da lista, o segundo fica no meio
        e os demais números entre os dois dados ficam nas pontas e repetem-se.
        Entrada: int,int ; Saída: list(int)'''

    if n1 < n2:
        return list(range(n1,n2)) + [n2] + list(range(n1,n2))[::-1]

    if n1 > n2:
        return list(range(n2+1,n1+1))[::-1]+ [n2] + list(range(n2+1,n1+1))
    else:
        return [n1]

##7)Colchão
def colchao(medidas,H,L):
    '''Funcao que retorna True ou False caso um colchão consiga passar, ou não
        por uma porta de dimensões H e L, dado as mesmas e a lista com dimensões
        do colchão D.
        Entrada: lista(float,float,float) ; Saída: int,int'''
    

    if list(medidas)[1] <= H:
        return True
    else:
        return False
