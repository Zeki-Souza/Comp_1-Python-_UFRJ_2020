##Questão 1:
def zodiaco(data):
    '''Função que retorna o sígno do Zodíaco Chinês, tendo como parâmetro o
    ano de nascimento.
      int -> str'''
    dias = data%12
    lista_ciclo = ['Macaco','Galo','Cão','Porco','Rato','Boi','Tigre','Coelho','Dragão','Serpente','Cavalo','Carneiro']
    lista_anos = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    x = lista_anos[dias]

    return lista_ciclo[x]
