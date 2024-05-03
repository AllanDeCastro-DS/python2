import os


def chamar_nome_do_app():
    print('''
    
  ____           _                              _        
 |  _ \ ___  ___| |_ __ _ _   _ _ __ __ _ _ __ | |_ ___  
 | |_) / _ \/ __| __/ _` | | | | '__/ _` | '_ \| __/ _ \ 
 |  _ <  __/\__ \ || (_| | |_| | | | (_| | | | | ||  __/ 
 |_|_\_\___||___/\__\__,_|\__,_|_|  \__,_|_| |_|\__\___| 
         | ____|_  ___ __  _ __ ___  ___ ___  ___                
        |  _| \ \/ / '_ \| '__/ _ \/ __/ __|/ _ \               
        | |___ >  <| |_) | | |  __/\__ \__ \ (_) |              
        |_____/_/\_\ .__/|_|  \___||___/___/\___/               
                   |_|                                          
            
            
            ''')

def finalizar_app():
    os.system('clear')
    chamar_nome_do_app()

restaurantes = [
    {'nome': 'coiso', 'categoria': 'opcao1', 'ativo': False},
    {'nome': 'coiso2', 'categoria': 'opcao2', 'ativo': False},
                 ]



def cadastrar_restaurante():
    finalizar_app()
    nome = input('Digite o nome do restaurante: \n')
    categoria = input('\nDigite a Categoria do restaurante: ')
    ativo = False
    restaurantes.append({'nome': nome, 'categoria': categoria, 'ativo':ativo})
    main()



def listar_restaurantes():
    finalizar_app()
    for restaurante in restaurantes:
        print(f'Nome: {restaurante["nome"]}, Categoria: {restaurante["categoria"]}, Ativo: {restaurante["ativo"]} \n')   
    main()




def ativar_restaurante():
    finalizar_app()
    nome = input('Digite o nome do restaurante a ativar: ')

    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            if restaurante['ativo'] == False:
                restaurante['ativo'] = True
                print(f'\nO restaurante {nome} foi Ativado')
                main()
            else:
                restaurante['ativo'] = False
                print(f'\nO restaurante {nome} foi Desativado. \n')
                main()



def escolher_opcoes():
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
            print('Opção inválida\n')

    except ValueError:
        print('Por favor, digite um número válido\n')




def main():
   
    escolher_opcoes();

if __name__ == "__main__":
    os.system('clear')
    chamar_nome_do_app()
    main();
