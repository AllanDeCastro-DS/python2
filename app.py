import os

def nome():
    print("Restaurante expresso");



def listar():
    print("1- Cadastrar Restaurante");
    print("2- listar Restaurantes");
    print("3- ativar Restaurante");
    print("4- sair\n");


def opcoes():
    
    opcao_digitada = int(input("Escolha um numero de 1 a 4; "));
    print("Você escolheu: ", opcao_digitada);
    if opcao_digitada == 1:
        print("Você escolheu 1- Cadastrar Restaurante\n")
    elif opcao_digitada ==2:
        print("Você escolheu 2- listar Restaurantes\n")
    elif opcao_digitada == 3:
        print("Você escolheu 3- ativar Restaurante\n")
    else:
        print("Você escolheu sair\n")
        os.system('cls')
        print('Fechando Aplicativo')

def main():
    print("Restaurante expresso");

if __name__ == "__main__":
    main()
    listar()
    opcoes()
