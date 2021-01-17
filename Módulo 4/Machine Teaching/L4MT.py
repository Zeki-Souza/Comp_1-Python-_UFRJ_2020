##Machine Teaching Lab 4

##1)Concatenação
def concatenacao(a, b):
    '''Funcao que, dado as strings a e b, retorna a concatenacao de ambas no
        formato abba. Entrada: str ; Saida: str.'''
    return a + b + b + a

##2)Substituição
def substitui(s,x,i):
    '''Funcao que recebe uma string 's', um numero inteiro 'i' que e entre 0
        e o comprimento da string. Retorne uma string igual a 's', onde a
        posicao i deve ser substituida pelo caractere x.
        Entrada: str, int ; Saida: str'''
    
    novastring = s[0:i] + str(x) + s[i+1:]
    
    return novastring

##3)String Recursiva
def recursiva(s):
    '''Funcao que recebe uma string e receba a mesma dentro de si mesma.
        Entrada: str ; Saida: str.'''
    return s[0: len(s)//2] + s + s[len(s)//2:]
   

##4)Hashtag
def hashtag(s):
    '''Funcao que recebe uma string e insira o caractere '#' no inicio, meio
        e fim da mesma. Entrada: str ; Saida: str'''
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'

##5)Numero de Dias
def diff_datas(data1,data2):
    '''Funcao que recebe duas datas no formato DD/MM/AA, onde a segunda e maior
        que a primeira, e que calcula quantos dias passaram entre ambas.'''
    d1 = int(data1[:2])
    m1 = int(data1[3:5])
    a1 = int(data1[6:])

    d2 = int(data2[:2])
    m2 = int(data2[3:5])
    a2 = int(data2[6:])
        
    conta1 = d1 + ((m1-1)*30)
    conta2 = d2 +((m2-1)*30)
    if a2 ==a1:
        return conta2 - conta1

    elif (m1 == m2):
        if (d2>d1):
            return ((a2-a1)*365 + (d2-d1))
        else:
            return ((a2-a1)*365 + (d1-d2))

    elif (m1 < m2):
        return ((a2-a1)*365 + (conta2 - conta1))

    elif (m1 > m2):
        return ((a2-a1)*365 -(conta1 - conta2))

##6)Filtragem
def filtra_pares(fp):
    '''Funcao que recebe uma tupla de quatro inteiros e
        que retorna apenas os pares na mesma'''
    t = ( )
    
    if fp[0] %2 == 0:
             t = t +(fp[0],)
    else:
             t = t
    if fp[1] %2 == 0:
             t = t +(fp[1],)
    else:
             t = t
    if fp[2] %2 == 0:
             t = t +(fp[2],)
    else:
             t = t
    if fp[3] %2 == 0:
             t = t +(fp[3],)
    else:
             t = t
    return t

##7)Dectando Colisões com Tuplas
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
        tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
    if (x_sup_dir1 < x_inf_esq2 or x_sup_dir2 < x_inf_esq1 or y_sup_dir1 < y_inf_esq2 or y_sup_dir2 < y_inf_esq1):
        return False
    else:
        return True
