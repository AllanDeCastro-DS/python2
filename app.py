import os




def chamar_nome_do_app():
    '''
    Função que mostra o nome do aplicativo no terminal
    '''
    print('''
    

  _____           _                              _                              
 |  __ \         | |                            | |                             
 | |__) |___  ___| |_ __ _ _   _ _ __ __ _ _ __ | |_ ___                        
 |  _  // _ \/ __| __/ _` | | | | '__/ _` | '_ \| __/ _ \                       
 | | \ \  __/\__ \ || (_| | |_| | | | (_| | | | | ||  __/                       
 |_|__\_\___||___/\__\__,_|\__,_|_|  \__,_|_| |_|\__\___|_                _____ 
 |  ____|                                        /\   | | |              / ____|
 | |__  __  ___ __  _ __ ___  ___ ___  ___      /  \  | | | __ _ _ __   | |     
 |  __| \ \/ / '_ \| '__/ _ \/ __/ __|/ _ \    / /\ \ | | |/ _` | '_ \  | |     
 | |____ >  <| |_) | | |  __/\__ \__ \ (_) |  / ____ \| | | (_| | | | | | |____ 
 |______/_/\_\ .__/|_|  \___||___/___/\___/  /_/    \_\_|_|\__,_|_| |_|  \_____|
             | |                                                                
             |_|                                                                

            ''')


def subtitulo(texto):
    """
    Imprime um texto com uma linha de igual (=) acima e abaixo.

    Esta função imprime um texto com uma linha de igual (=) acima e abaixo do texto,
    criando um efeito de título.

    Parameters
    ----------
    texto : str
        O texto a ser impresso.

    Returns
    -------
    None

    """
    linha = '='*len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    '''
    Esta função limpa o conteudo do terminal e mostra o titulo no terminal
    '''
    os.system('clear')
    chamar_nome_do_app()

restaurantes = [
    {'nome': 'coiso', 'categoria': 'opcao1', 'ativo': False},
    {'nome': 'coiso2', 'categoria': 'opcao2', 'ativo': False},
                 ]



def cadastrar_restaurante():

    
    finalizar_app()
    subtitulo('Cadastrar Restaurante')
    nome = input('Digite o nome do restaurante: \n')
    categoria = input('\nDigite a Categoria do restaurante: ')
    
    restaurantes.append({'nome': nome, 'categoria': categoria, 'ativo':False})
    main()



def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados.

    Esta função lista todos os restaurantes cadastrados, exibindo o nome, categoria e status de ativação de cada restaurante.

    Returns
    -------
    None

    """
    finalizar_app()
    subtitulo('Lista de Restaurantes')
    

    for restaurante in restaurantes:
        nome = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = 'Ativado' if restaurante["ativo"] else 'Desativado'

        print(f'Nome: {nome}, Categoria: {categoria}, Ativo: {ativo} \n')
    main()




def ativar_restaurante():
    """
    Essa função permite ativar ou desativar um restaurante da lista de restaurantes.
    Ela exibe a lista de restaurantes e pede ao usuário que informe o nome do restaurante a ser ativado ou desativado.
    Se o restaurante estiver inativo, a função o ativa e vice-versa.
    """
    finalizar_app()
    subtitulo('Ativar Restaurante')
    for restaurante in restaurantes:
        print(f'O restaurante {restaurante["nome"]} está com Status ativo: {restaurante["ativo"]}\n')
    nome = input('Digite o nome do restaurante a ativar: ')

    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            if restaurante['ativo'] == False:
                restaurante['ativo'] = True
                finalizar_app()
                print(f'\nO restaurante {nome} foi Ativado')
                main()
            elif restaurante['ativo'] == True:
                restaurante['ativo'] = False
                finalizar_app()
                print(f'\nO restaurante {nome} foi Desativado. \n')
                main()
            elif nome == '':
                finalizar_app()
                main()
            else:
                print(f'\nO restaurante {nome} não foi encontrado. \n')
                main()



def escolher_opcoes():
    '''
     Esta função apresenta ao usuário 4 opções para escolher:
    1 - Cadastrar restaurante
    2 - Listar restaurantes
    3 - Ativar restaurante
    4 - Sair do programa

    inputs:
        - opção_digitada 
    output:
        - dependendo do numero digitado ira executar uma das opções exibidas anteriormente
    '''
    print('\n1- cadastrar restaurante')
    print('2- listar restaurantes')
    print('3- ativar restaurante')
    print('4- sair do programa\n')

    try:
        opcao_digitada = int(input('Escolha uma opção: '))
        print('Você selecionou:', opcao_digitada, '\n')

        if opcao_digitada == 1:
            cadastrar_restaurante()
        elif opcao_digitada == 2:
            listar_restaurantes()
        elif opcao_digitada == 3:
            ativar_restaurante()
        elif opcao_digitada == 4:
            print('Você escolheu sair do programa\n')
        else:
            finalizar_app()
            print('Opção inválida\n')
            main()

    except ValueError:
        finalizar_app()
        print('Por favor, digite um número válido\n')
        main()




def main():
   
    escolher_opcoes();
    """
    Função principal do programa.

    Chama a função escolher_opcoes para iniciar o fluxo de execução do programa.

    Returns:
        None
    """
if __name__ == "__main__":
    os.system('clear')
    chamar_nome_do_app()
    main();
