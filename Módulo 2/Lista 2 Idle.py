
import math

##Questão 1:
##a):
def media3(n1,n2,n3):
    '''funcao que retorna a media de tres numeros inteiros, dados por n1,n2 e n3
        float, float, float -> float'''
    return (n1 + n2 + n3)/3 
##b):
def difmair(n1,n2,n3):
    '''funcao que retorna, dados os numeros n1,n2 e n3, a diferença do maior
        deles com a media. float, float, float -> float'''
    return max(n1,n2,n3) - media3(n1,n2,n3)

##c):
def sommin(n1,n2,n3):
    '''funcao que retorna, dados os numeros n1,n2 e n3, a soma do menos deles
        com a media. float, float, float -> float'''
    return min(n1,n2,n3) + media3(n1,n2,n3)


##Questão 2:
def delta(a,b,c):
    '''funcao que dado os parametros a,b,c calcula o delta de um polinomio de
        segundo grau. int, int, int - float'''
    return b**2 - 4*a*c
##a):
def deltasoma(a,b,c):
    '''funcao que retorna a soma entre o delta e uma primeira raiz
        de uma equacao de segundo grau, dado os coeficientes a,b,c
            float, float, float -> float'''
    return -b + math.sqrt(delta(a,b,c))/(2*a) + delta(a,b,c)
##b):
def deltasub(a,b,c):
    '''funcao que retorna a subtracao entre o delta e uma segunda raiz
        de uma equacao de segundo grau, dado os coeficientes a,b,c
            float, float, float -> float'''
    return - b + math.sqrt(delta(a,b,c))/(2*a) + delta(a,b,c)
        

##Questão 3:
##a)
def ntermos(vi,vf,r):
    '''funcao que calcula o numero de termos dado o valor inicial vi,
        valor final vf e razao r
            int,int,int -> int'''
    return (vf - vi)/r + 1
##b)
def somapa(vi,vf,r):
    '''funcao que calcula a soma de uma progressao aritimetica, dado o
        valor inicial vi, o valor final vf e a razao r
                int, int, int, -> int'''
    return (vi + vf) * ntermos(vi,vf,r)/2


##Questão 4:
##a)
def pi():
    '''funcao que retorna o valor de pi, sendo 3.14
        Sem parâmetro de entrada -> float'''
    return 3.14
##b)
def abcil(r):
    '''funcao que retorna a area de base de um cilindro, tendo como parametros
       o  valor pi e o raio r;  float -> float'''
    return 2*pi()*(r**2)
##c)
def alcil(r,al):
    '''funcao que retorna a area lateral de um cilindro, dado os parametros
        o raio r e a altura al; float,float -> float'''
    return 2*pi()*r*al
##d)
def atcil(r,al):
    '''funcao que retorna a area total de um cilindro, dado os parametros
        raio r, altura al e usando as funcoes anteriores de area lateral
            e area de base; float, float -> float'''
    return 2* abcil(r)+ alcil(r,al)


##Questão 5:
##a)
def hipote(a,b):
    '''funcao que retorna o valor da hipotenusa de um triangulo retangulo
        dado os catetos a e b; float,float -> float'''
    return math.sqrt(a**2 + b**2)
##b)
def dispo(x1,y1,x2,y2):
    '''funcao que calcula a distancia entre dois pontos em uma plano dado suas
        coordenadas x1, y1, x2, y2; float,float,float,float -> float'''
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
##c)
def peritri(a,b):
    '''funcao que retorna o perimetro de um triangulo reto dado os catetos
        a e b, usando tambem a funcao da hipotenusa; float,float -> float '''
    return a + b + hipote(a,b)
##d)
def somsencos2(x):
    '''funcao que caulcua a soma do quadrado do seno e do quadrado do cossenos
        de um angulo x. int -> int  '''
    return (math.sin(math.radians(x))**2) + (math.cos(math.radians(x))**2)

##e)
def comcir(r):
    '''funcao que retorna o comprimento de um circulo, dado o raio e
        usando a funcao que retorna o valor de pi
        float -> float'''
    return 2*math.pi*r


##Questão 6:
def setcirc (r,ang=60):
    ''' funcao que retorna a area de um setor circular, dado seu raio e
        o angulo, com argumento default sendo igual a 360
            float -> float'''
    return ang * (3.14* r**2)/360


##Questão 7:
##a)
def bombom(d,p):
    '''funcao que retorna o troco em dinheiro que Pedrinho recebe ao comprar
        o maior numero de bombons possiveis dado o seu dinheiro, d,
            e o preco dos bombons p. float,float -> float'''
    return d%p
##b)
def IMC(AL,PE):
    '''funcao que calcula o Indice de Massa Corporal de uma pessoa,
        dados sua altura AL e seu peso PE
            float,float -> float'''
    return PE/ (AL**2)
##c)
def viagem(pas):
    '''funcao que retorna o numero de carros necessarios para transportar
        um numero dado de passageiros, pas, de modo que 1 carro pode transportar
            apenas 5 passageiros. int,int - int'''
    return math.ceil(pas/5)


##Questão 8:
##1)
def compcirc(r):
    '''funcao que retorna o comprimento de um circulo, dado o raio e
        usando a funcao que retorna o valor de pi
        float - float'''
    return 2*3.14*r
##2)
def voltas(disp,rp):
    '''funcao que retorna o numero de voltas que um atleda da numa pista
        dado o raio da pista rp e a distancia que ele percorreu
            float,float -> float'''
    return disp/compcirc(rp)


##Questão 9:
def bolos(A,B,C):
    '''funcao que retorna a quantidade maxima de bolos que Joao pode fazer
        tendo como paramentros A xicaras e farinha, B ovos e C colheres de leite
            float,float,float -> int'''
    return (A/2 + B/3 + C/5)//3

