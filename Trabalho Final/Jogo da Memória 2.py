def gera_matriz():
    """Gera uma matriz 4x4 aleatória
    cujas entradas são os números de 1 a 8,
    cada um com 1 repetição"""
    from random import randint
    lista_de_números = 2*list(range(1,9))
    matriz = []
    for posição_linha in range(4):
        # aqui a tarefa é gerar e guardar 1 linha
        linha = []
        for posição_coluna in range(4):
            # aqui a tarefa é gerar e guardar 1 elemento
            posição_sorteada = randint(0,len(lista_de_números)-1)
            elemento = list.pop(lista_de_números,posição_sorteada)
            list.append(linha,elemento)
        list.append(matriz,linha)
    return matriz

def mostra_situação(matriz,posições_para_abrir):
    """Mostra matriz com asteriscos e posições 'abertas'
    dependendo se o número naquela posição já foi acertado
    ou não"""
    for posição_linha in range(4):
        for posição_coluna in range(4):
            elemento = matriz[posição_linha][posição_coluna] 
            if (posição_linha,posição_coluna) in posições_para_abrir:
                print(elemento, end=' ')
            else:
                print('*', end=' ')
        print()

def recebe_jogada(posições_abertas):
    """Interage com o usuário para receber uma jogada
    válida, i.e., uma que não coincide com uma casa
    já aberta antes"""
    posição_linha = int(input("Qual linha (0 a 3)? "))
    posição_coluna = int(input("Qual coluna (0 a 3)? "))
    while posição_linha not in (0,1,2,3) or posição_coluna not in (0,1,2,3) or (posição_linha,posição_coluna) in posições_abertas:
        posição_linha = int(input("Inválido! Qual linha (0 a 3)? "))
        posição_coluna = int(input("Inválido! Qual coluna (0 a 3)? "))
    return posição_linha, posição_coluna

def main():
    """JOGO DA MEMÓRIA"""
    matriz = gera_matriz()
    posições_abertas = []
    contador = 0
    print(matriz)
    print()
    while len(posições_abertas) < 16:
        # o jogo ainda não acabou
        contador += 1
        mostra_situação(matriz,posições_abertas)
        primeira_jogada = recebe_jogada(posições_abertas)
        intermediário = posições_abertas + [primeira_jogada]
        mostra_situação(matriz,intermediário)
        segunda_jogada = recebe_jogada(intermediário)
        final = intermediário + [segunda_jogada]
        mostra_situação(matriz,final)
        elemento_1 = matriz[primeira_jogada[0]][primeira_jogada[1]]
        elemento_2 = matriz[segunda_jogada[0]][segunda_jogada[1]]
        if elemento_1 == elemento_2:
            # ACERTO!
            posições_abertas = final
        print('-'*10)
    print(str.format('Acabou! Foram {} jogadas',contador))

if __name__ == '__main__':
    main()
