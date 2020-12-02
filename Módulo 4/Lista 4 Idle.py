

import math
##Questão 1:
def Siga(nomea,n1,n2,n3):
    '''Função que recebe o nome de um aluno e suas três
    notas n1,n2,n3 e retorna o nome do mesmo,
    sua media e sua situacao dependente de sua media.
    Entrada: str, float, float, float,
    Saida: tupla(str,float,bool).'''
    media= (n1+n2+n3)/3

    if media>=7:
        return (nomea, media, ' Aprovado')
    elif 7> media >=5:
        return (nomea, media, ' Aprovado')
    else:
        return (nomea, media, ' Reprovado')

##Questão 2:
##2.1
def quadrante1(radianos):
    '''Função que, dado um angulo qualquer,retorne um
    inteiro entre 1 e 4 que represente em qual quadrante
    esse ângulo se encontra. A função também deve ter
    um parâmento booleno que indica se o ângulo em questão
    foi medido em graus ou radianos
    (True para graus e False para Radianos)e caso o ângulo
    encontre-se no limite entre dois quadrantes, a
    resposta deve ser o quadrante de menor numeraçao.
    float -> int'''
    extrar = radianos//(2*math.pi)
    
    if (0 < radianos <= math.pi/2):
        return 1
    elif (math.pi/2 < radianos <= math.pi):
        return 2
    elif (math.pi < radianos <= (3*math.pi)/2):
        return 3
    elif ((3*math.pi)/2 < radianos <= 2*math.pi):
        return 4
    else:
        return extrar
    
##2.2
def quadrante2(angulo):
    '''Função que, dado um angulo qualquer, retorne um
    inteiro entre 1 e 4 que represente em qual quadrante
    esse ângulo se encontra. A função também deve ter
    um parâmento booleno que indica se o Ângulo em questão
    foi medido em graus ou radianos
    (True para graus e False para Radianos)e caso o
    Ângulo encontre-se no limite entre dois quadrantes,
    a resposta deve ser o quadrante de menor numeracao.
    int -> int'''
    extraa = angulo//360
    
    if (0 <= angulo <= 90):
        return 1
    elif (90 < angulo <= 180):
        return 2 
    elif (180 < angulo <= 270):
        return 3
    elif (270 < angulo <= 360):
        return 4
    else:
        return extraa - 1
