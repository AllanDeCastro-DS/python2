import os

def finalizar_app():
    os.system('clear')
    print('finalizando app\n')

def chamar_nome_do_app():
    print('restaurante expresso\n')

def escolher_opcoes():
    print('1- cadastrar restaurante')
    print('2- listar restaurantes')
    print('3- ativar restaurante')
    print('4- sair do programa\n')

def cadastrar_restaurante():
    nome = input('Digite o nome do restaurante: ')
    localizacao = input('Digite a localização do restaurante: ')

    restaurantes.append({'nome': nome, 'localizacao': localizacao})

def listar_restaurantes():
    for restaurante in restaurantes:
        print(f'Nome: {restaurante["nome"]}, Localização: {restaurante["localizacao"]}')

def ativar_restaurante():
    nome = input('Digite o nome do restaurante a ativar: ')

    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            restaurante['ativo'] = True
            print(f'Restaurante {nome} ativado com sucesso!')
            break

restaurantes = []

while True:
    finalizar_app()
    chamar_nome_do_app()
    escolher_opcoes()

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
            break
        else:
            print('Opção inválida\n')

    except ValueError:
        print('Por favor, digite um número válido\n')
        