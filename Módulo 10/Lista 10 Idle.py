

##Questão 1:
def repetidos(listaR):
    '''Função que receba uma lista de números, e retorne o número
    de vezes ocorre uma série de números iguais.
    list -> int'''
    cont = 0
    j = 0
    while j < len(listaR):
        if listaR[j] == (listaR[j-1]):
            listaR.count(listaR[j])
            cont += 1
        j += 1
    return cont

import random
def lancamento_dado():
    '''Função que lê a série de lançamentos de um dado, guarda-os numa lista
    e conta o número de ocorrências de séries de faces repetidas.
    Sem parâmetro de entrada -> str,int,str'''
    lista_lancados = []
    lancamentos = int(input("Informe os Lançamentos: "))
    for i in range(lancamentos):
        lista_lancados.append(random.randint(1,6))
    print("A lista de números é: ", lista_lancados)
    print("Nesta lista existem " + str(repetidos(lista_lancados)) + " séries de números iguais.")
    

        


##Questão 2:
def leitura_i():
    '''Função que lê um código i, em um intervalor de 1 a 4, e 3 valores a,b,c inteiros
    positivos com a<b e; Se  i=1, retornar a área do trapézio de bases a e b
    e altura c e mostrar junto com os valores lidos.
    Se  i=2, calcular a *a, b*b e c*c e mostrar os valores lidos;
    Se i=3, calcular a média aritimética entre a,b,c e mostrar os valores lidos;
    Se i=4, calcular e mostrar a soma dos inteiros de a inclusive até b com a variação até
    a c;
    Sem parâmetro de entrada -> int,int,int,int .'''
    i = input("Escolha um cógido de 1 a 4: ")
    a = int(input("Informe o valor de a: "))
    b = int(input("Informe o valor de b(b>a): "))
    c = int(input("Informe o valor de c: "))
    if b < a:
        print("b não pode ser menor que a")
        return
    print("Valor a = ", str(a))
    print("Valor b = ", str(b))
    print("Valor c = ", str(c))
        #Função para i = 1
    def funcao_um(a,b,c):
        return ((a+b)*c)/2

    #Função para i = 2
    def funcao_dois(a,b,c):
        return a*a,b*b,c*c

    #Função para i = 3
    def funcao_tres(a,b,c):
        return (a+b+c)/3

    #Função para i = 4
    def funcao_quatro(a,b,c):
        soma = 0
        while a < b:
            soma += a
            a += c
        return soma
    if i == "1":
        print(funcao_um(a,b,c))
    elif i == "2":
        print(funcao_dois(a,b,c))
    elif i == "3":
        print(funcao_tres(a,b,c))
    elif i == "4":
        print(funcao_quatro(a,b,c))
    else:
        print("Não foi escolhido um código correto.")


    
##Questão 3:
def buscaSetor():
    '''Função que, a partir de uma matriz com dados de funcionários, busca os dados
    a partir do seu setor no emprego e retorna a matriz com os contatos cujos
    funcionários pertencem a tal setor.
    Sem parâmetro de entrada -> Matriz(str)'''
    busca = []
    matriz = []
    registro = 3
    while registro > 0:
        nome = input("Digite o nome do funcioário: ")
        matricula = input("Digite a matrícula do funcionário: ")
        setor = input("Digite o setor do funcionário: ")
        tel = input("Digite o telefone no funcionário: ")
        matriz.append([nome, matricula, setor, tel])
        registro -= 1
        
    setor = input("Digite o setor desejado para á busca: ")
    for linha in range(len(matriz)):
        if (matriz[linha][2] == setor):
            busca.append(matriz[linha])
    if (len(busca) == 0):
        return "Nenhum registro foi encontrado."
    print (busca)

