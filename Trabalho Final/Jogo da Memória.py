##1)

def fazmatriz():
    '''Faz uma matriz 4x4 aleatória entre os números 1 a 8, onde cada
    um repete uma vez.
    Sem entrada -> matriz'''
    from random import randint
    lista_num = 2*list(range(1,9))
    matriz = []
    for pos_linha in range(4):
        linha = []
        for pos_coluna in range(4):
            sorteado = randint(0,len(lista_num)-1)
            elemento = list.pop(lista_num, sorteado)
            list.append(linha,elemento)
        list.append(matriz,linha)
    return matriz

def asteristicos(matriz,pos_abrir):
    ''' Faz a matriz com asteriscos e posições abertas,
    dependendo se o número naquela posição já foi acertado
    ou não'''
    for pos_linha in range(4):
        for pos_coluna in range(4):
            elemento = matriz[pos_linha][pos_coluna] 
            if (pos_linha,pos_coluna) in pos_abrir:
                print(elemento, end=' ')
            else:
                print('*', end=' ')
        print()

def jogada(pos_abertas):
    '''Interage com o usuário e recebe uma jogada válida, ou seja, uma
    que já não fora aberta antes e que exista.'''
    pos_linha = int(input("Qual linha deseja escolher? (0 a 3): "))
    pos_coluna = int(input("Qual coluna deseja escolher? (0 a 3): "))
    while pos_linha not in (0,1,2,3) or pos_coluna not in (0,1,2,3) or (pos_linha,pos_coluna) in pos_abertas:
        pos_linha = int(input("Opção inválida! Favor escolher novamente a linha desejada: "))
        pos_coluna = int(input("Opção inválida! Favor escolher novamente a coluna desejada: "))
    return pos_linha, pos_coluna

def main():
    '''Jogo da Memória'''
    matriz = fazmatriz()
    pos_abertas = []
    contador = 0
    print("Memorize os números: ",matriz)
    print()
    while len(pos_abertas) < 16:
        contador += 1
        asteristicos(matriz,pos_abertas)
        jogo_um = jogada(pos_abertas)
        intermed = pos_abertas + [jogo_um]
        asteristicos(matriz,intermed)
        jogo_dois = jogada(intermed)
        final = (intermed + [jogo_dois])
        asteristicos(matriz,final)
        elemento1 = matriz[jogo_um[0]][jogo_um[1]]
        elemento2 = matriz[jogo_dois[0]][jogo_dois[1]]
        if elemento1 == elemento2:
            pos_abertas = final
        print('-'*10)
    print(str.format("Parabéns,você terminou! Foram {} jogadas", contador))

if __name__ == '__main__':
    main()
