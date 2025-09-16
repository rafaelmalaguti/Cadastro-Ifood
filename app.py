import os 

restaurantes = [{'nome': 'Parking', 'categoria': 'Pizza', 'ativo':False},
                {'nome': 'Kombuca', 'categoria': 'Lanches', 'ativo':True},
                {'nome': 'Burgão', 'categoria': 'Hamburguer', 'ativo':False}]

def exibir_nome_app(): 
    print('============================')
    print('           𝕀𝔽𝕆𝕆𝔻')
    print('============================\n')

def exibir_opcoes():
    print('1.Cadastro Restaurante')
    print('2.Listar Restaurantes')
    print('3.Alternar Estado do Restaurante')
    print('4.Sair\n')

def saindo_app():
     os.system('cls') 
     print('Saindo do app...')

def opcao_invalida():
    os.system('cls')
    print('Opção inválida, tente novamente\n')
    voltar_ao_menu()
    

def voltar_ao_menu():
    input('\nAperte ENTER para voltar ao menu principal')
    os.system('cls')
    main()

def cadastrar_restaurante():
    os.system('cls')
    print('=' * 23)
    print('Cadastro de Restaurante')
    print('=' * 23)
    print('')
    nome_restaurante = input('Nome do Restaurante: ')
    categoria = input(f'Categoria do Restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante ({nome_restaurante}) foi cadstrado com sucesso!\n')
    voltar_ao_menu()
    
def alternar_restaurante():  
    os.system('cls')
    print('=' * 19)
    print('Ativar Restaurante') 
    print('=' * 19) 
    print('')
    nome_restaurante = input('Nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante ({nome_restaurante}) está ativado com sucesso' if restaurante['ativo'] else f'O restaurante ({nome_restaurante}) está desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante ({nome_restaurante}) não foi encontrado')
    voltar_ao_menu()

def listar_restaurantes():
    os.system('cls')
    print('=' * 22)
    print('Lista de Restaurantes')
    print('=' * 22)
    print('')
    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu()
    


def esolher_opcao():
    try:
        Opção = input('Escolha uma opção: ')
        print(f'Voce escolheu a opção: {Opção}')

        if Opção == '1':
           cadastrar_restaurante() 
        elif Opção == '2':
            listar_restaurantes()
        elif Opção == '3':
            alternar_restaurante()
        elif Opção == '4':
            saindo_app() 
        else:
            opcao_invalida() 
    except:
        opcao_invalida()
        
        
def main():
    exibir_nome_app()
    exibir_opcoes()
    esolher_opcao()

if __name__ == '__main__':
    main()
    

