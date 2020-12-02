import math

##Questão 1:
def valabsol(x):
    '''funcao que retorna o valor absoluto de
    um numero fornecido x
        float -> float'''
    if x<=0:
            return -x
    else:
        return x

##Questão 2:
def delta(a,b,c):
    '''funcao que calcula o delta de uma função do
    segundo grau, dado os tres
    coeficientes a,b,c.
    float, float , float -> float'''
    return pow(b,2)- 4*a*c

def raizeq(a,b,c):
    '''funcao que retorna quantas sao as raízes
    de uma equação de segundo grau,
    dado os tres coeficientes a,b,c.
    float, float, float -> float'''
    if delta(a,b,c)>0:
        return (-b + math.sqrt(delta(a,b,c)))/ 2*a, (-b - math.sqrt(delta(a,b,c)))/ 2*a
    elif delta(a,b,c)==0:
        return -b//2*a
    else:
        return 'Nao existem raizes'

##Questão 3:
def felicitacoes(msg,n):
    '''funcao que recebe uma mensagem de felicitacoes
    msg, que é repetida n vezes.
    str,int -> string'''
    return str(msg) * n

##Questão 4:
def diamesano(D,M,A):
    '''funcao que recebe tres numeros inteiros d,m,a e
    retorna uma sequência de caracteres
    formatadas no padrão DD/MM/AA'.
    int, int, int -> string'''
    return str(D) + '/'+ str(M) +'/'+ str(A)

##Questão 5:
def figura(X):
    '''função que tem o comportamento
    da função matemática da figura da questão,
    dado X.
    float -> int '''
    if (X<=2):
        return X
    elif (2<= X <=3.5):
        return 2
    elif (3.5< X <= 5):
        return 3
    else:
        return (pow(X,2) - (10)*X+28)

##Exercicio 6:

##a)
def descontoinss(sb):
    '''função que retorna a taxa de desconto do imposto
    INSS de acordo com a tabela, e que tem como parâmetro
    o salário bruto sb.
    float -> float'''
    if (sb<= 2000.00):
        return sb*(6/100)
    elif (2000.00 < sb <= 3000.00):
        return sb*(8/100)
    else:
        return sb*(10/100)

##b)
def descontoir(sb):
    '''funcao que retorna a taxa de desconto do imposto
    de renda, de acordo com a tabela e tendo como
    parâmetro o salário bruto, sb.
    float -> float'''
    if (sb<= 2500.00):
        return sb* (11/100)
    elif (2500.00 < sb <= 5000.00):
        return sb* (15/100)
    else:
        return sb* (22/100)

##c)
def salliq(sb):
    '''funcao que calcula o salário líquido,
    diminuindo o salário bruto, sb, dos
    descontos pagos ao INSS e IR.
    float -> float'''
    return sb - ( descontoinss(sb) + descontoir(sb))
     

