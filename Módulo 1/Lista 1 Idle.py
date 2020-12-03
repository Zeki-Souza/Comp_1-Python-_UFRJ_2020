
##Questão 1:
def retangulo(x,y):
    """ funcao que retorna a area de um retangulo dado seus dois lados x e y """
    return x*y

##Questão 2:
def cubo(c):
    """ Funcao que retorna a area de um cubo, dado valor de sua aresta c """
    return c**3

##Questão 3:
def coroa(r1,r2):
    """ Funcao que retorna o valor da area da coroa ciruclar,
        dado a area dos ciruclos r1 e r2 """
    pi = 3.14
    area = pi*(r1**2 - r2**2)
    return area

##Questão 4:
def media (d,e):
    """ Funcao que retorna o valores da média entre dois numeros """
    return (d+e)/2

##Questão 5:
def ordenada(ab,k,p,t):
    """ Funcao que retorna a ordenada de uma funcao de segundo grau,
        e sua abscissa, dados os parametros k,p e t """
    return ab*k**2 + p*k+t

##Questão 6:
def medpond(n1,p1,n2,p2):
    """ Funcao que calcula a media ponderada de dois numeros
            pela ordem, n1 , p1, n2 e p2; onde n= numero e p= peso """
    return (n1*p1 + n2*p2)/(p1+p2)

##Questão 7:
def pg(q,n):
    """ Funcao que retorna o valor do erro da soma de uma PG infinita
        a partir de 1 e a soma de seus tres primeiros numeros,
            representados por Sf3 """
    Sinf = 1/(1-q)
    Sfin = 1*(1-q**n)/(1-q)
    Sf3 = 1*(1-q**3)/(1-q)
    return Sinf - Sfin, Sf3

##Questão 8:
def compra(vl):
    """ Funcao que calcula a gorjeta, dado o valor da compra e a
        porcentagem da gorjeta de 10% """
    return vl*0.1

##Questão 9:
def gorgeta(vc,gr):
    """ Funcao que retorna o valor da gorjeta, dado o
        valor da compra - vc ; e a porcentagem da gorgeta - gr """
    return vc*gr/100

##Questão 10:
def SF(Si,m,j):
    """ Funcao que retorna o saldo final de uma conta, dado o saldo inicial - Si
       o numero de meses - m e a taxa de juros - j """
    return Si*(1+j*m/100)

##Questão 11:
def distcor(vcor,larg,vbar):
    """ Funcao que retorna a distancia que a correnteza arrasta um barco,
        dado a velocidade da correnteza - vcor, a largura do rio - latg, e
        a velocidade do barco perpendicular a correnteza - vbar """
    tp = larg/vbar
    return vcor*tp

