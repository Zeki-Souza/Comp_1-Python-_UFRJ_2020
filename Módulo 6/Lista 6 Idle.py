

##1) Aplicativo de Celular:
##As informações de cada contato é armazenada em uma lista;
##A única informação obrigatória é o nome;
##A agenda comporta números de telefone, e-mail e Instagram;
##Os números de telefone são armazenados em listas;


##a)Criar um contato novo:

def contato_novo(nome,telefones,email,instagram):
    '''Função que recebe uma lista com os dados
    (nome,telfones,e-mail e instagram), e retorna
    uma lista com os tais dados.
    list(str, str, str, str) -> list(str, str, str,str)'''
    contato = []
    list.insert(contato,0,nome)
    list.insert(contato,1,[telefones])
    list.insert(contato,2,email)
    list.insert(contato,3,instagram)

    return contato

##b)Atualizar um contato:


def att(contatos,I,info):
    '''Função que, tendo como base a lista anterior,
    onde contatos é igual a mesma, de dados salvos de
    um contato, atualiza-o com informações novas.
    Os parâmetros são: I, índice, que indica qual
    informação deve  ser alterada. E info, que indica
    qual informação deve ser alterada.
    list, int, str -> list(str, str, str)'''
    
    
    if I == 0:
        list.insert(contatos,info,0)
        return contatos
    elif I == 1:
        if info == contatos[1]:
            return contatos
        else:
            list.insert(contatos,1,info)
            return contatos
    elif I == 2:
        list.insert(contatos,2,info)
        return contatos
    elif I == 3:
        list.insert(contatos,3,info)
        return contatos
    else:
        return contatos
   
