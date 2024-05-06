import os


def chamar_nome_do_app():
    print('''
    
  ____           _                              _        
 |  _ \ ___  ___| |_ __ _ _   _ _ __ __ _ _ __ | |_ ___  
 | |_) / _ \/ __| __/ _` | | | | '__/ _` | '_ \| __/ _ \ 
 |  _ <  __/\__ \ || (_| | |_| | | | (_| | | | | ||  __/ 
 |_|_\_\___||___/\__\__,_|\__,_|_|  \__,_|_| |_|\__\___| 
        _______
        | ____|_  ___ __  _ __ ___  ___ ___  ___                
        |  _| \ \/ / '_ \| '__/ _ \/ __/ __|/ _ \               
        | |___ >  <| |_) | | |  __/\__ \__ \ (_) |              
        |_____/_/\_\ .__/|_|  \___||___/___/\___/               
                   |_|                                          
            
            
            ''')


def subtitulo(texto):
    linha = '='*len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
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
    finalizar_app()
    subtitulo('Lista de Restaurantes')
    

    for restaurante in restaurantes:
        nome = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = 'Ativado' if restaurante["ativo"] else 'Desativado'

        print(f'Nome: {nome}, Categoria: {categoria}, Ativo: {ativo} \n')
    main()




def ativar_restaurante():
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

if __name__ == "__main__":
    os.system('clear')
    chamar_nome_do_app()
    main();
