
##Questão 1:
def retangulo(x,y):
    """Função que retorna a área de um
    retângulo dado seus dois lados x e y
    float, float -> float"""
    return x*y

##Questão 2:
def cubo(c):
    """Função que retorna a área de um cubo,
    dado valor de sua aresta c
    float -> float"""
    return c**3

##Questão 3:
def coroa(r1,r2):
    """Função que retorna o valor da área
    da coroa ciruclar, dado a área
    dos ciruclos r1 e r2
    float, float -> float"""
    pi = 3.14
    area = pi*(r1**2 - r2**2)
    return area

##Questão 4:
def media (d,e):
    """Funcao que retorna o valores da
    média entre dois numeros
    float, float -> float"""
    return (d+e)/2

##Questão 5:
def ordenada(ab,k,p,t):
    """Função que retorna a ordenada de uma
    função de segundo grau e sua abscissa,
    dados os parâmetros k,p e t
    float, float, float, float -> float"""
    return ab*k**2 + p*k+t

##Questão 6:
def medpond(n1,p1,n2,p2):
    """Função que calcula a média ponderada de dois números
    pela ordem, n1 , p1, n2 e p2;
    onde n= numero e p= peso
    float, float, float, float -> float"""
    return (n1*p1 + n2*p2)/(p1+p2)

##Questão 7:
def pg(q,n):
    """Função que retorna o valor do erro da soma
    de uma PG infinita a partir de 1 e a soma
    de seus tres primeiros números, representados
    por Sf3
    int, int -> int"""
    Sinf = 1/(1-q)
    Sfin = 1*(1-q**n)/(1-q)
    Sf3 = 1*(1-q**3)/(1-q)
    return Sinf - Sfin, Sf3

##Questão 8:
def compra(vl):
    """Função que calcula a gorjeta, dado o valor
    da compra e a porcentagem da gorjeta de 10%
    float -> float"""
    return vl*0.1

##Questão 9:
def gorgeta(vc,gr):
    """Funçãoo que retorna o valor da gorjeta,
    dado o valor da compra vc, e a porcentagem
    da gorgeta, gr
    float, float -> float"""
    return vc*gr/100

##Questão 10:
def SF(Si,m,j):
    """Funçãoo que retorna o saldo final de uma
    conta, dado o saldo inicial, Si
    o numero de meses - m e a taxa de juros, j
    float, int, float -> float """
    return Si*(1+j*m/100)

##Questão 11:
def distcor(vcor,larg,vbar):
    """Função que retorna a distancia que a
    correnteza arrasta um barco, dado a velocidade
    da correnteza, vcor, a largura do rio, latg e
    a velocidade do barco perpendicular
    a correnteza, vbar.
    float, float, float -> float"""
    tp = larg/vbar
    return vcor*tp

