AGENDA = {}


# Métodos da agenda
def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)


def buscar_contato(contato):
    x = contato.capitalize()
    if x in AGENDA:
        print(f'\n{x}')
        print(f'Telefone: {AGENDA[x]["tel"]}')
        print(f'Email: {AGENDA[x]["email"]}')
        print(f'Endereço: {AGENDA[x]["endereco"]}')
        print('--------------------------')
    else:
        print(f'\n Contato não encontrado!')


def incluir_editar_contato(nome, tel, email, endereco):
    x = nome.capitalize()
    AGENDA[x] = {
        'tel': tel,
        'email': email,
        'endereco': endereco,
    }
    salvar_agenda()
    print(f'\n>>>>>Contato {x} adicionado com sucesso')



def excluir_contato(contato):
    try:
        x = contato.capitalize()
        AGENDA.pop(x)
        salvar_agenda()
        print(f'\n>>>>> O contato {x} foi removido da agenda!')
    except KeyError:
        print(f'\n>>>>> Erro ao remover, Contato Inexistente!')
    except Exception as error:
        print(f'Um erro inesperado ocorreu!')


def imprimir_menu():
    print(f'-----------------------------------------'
          f'\n1 - Mostrar todos os contatos da agenda'
          f'\n2 - Buscar Contato'
          f'\n3 - Incluir Contato'
          f'\n4 - Editar Contato'
          f'\n5 - Excluir Contato'
          f'\n6 - Exportar Contatos para CSV'
          f'\n7 - Importar Contatos'
          f'\n0 - Fechar Agenda'
          f'\n-----------------------------------------')


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                tel = AGENDA[contato]['tel']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato},{tel},{email},{endereco}\n')
        print(f'>>>>> Agenda exportada com sucesso')
    except Exception as error:
        print(f'**Erro: {error}')


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, tel, email, endereco)

    except FileNotFoundError:
        print(f'***** Arquivo não encontrado')
    except Exception as error:
        print(f'Um erro inesperado aconteceu {error}')


def ler_detalhes_contato():
    tel = input('Digite o telefone:')
    email = input('Digite o email:')
    endereco = input('Digite o endereço:')
    return tel, email, endereco


def salvar_agenda():
    exportar_contatos('database.csv')


def carregar_agenda():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'tel': tel,
                    'email': email,
                    'endereco': endereco,
                }
        print(f'>>>>Base de dados carregada com sucesso'
              f'\n* {len(AGENDA)} contatos carregados')
    except FileNotFoundError:
        print(f'***** Arquivo não encontrado')
    except Exception as error:
        print(f'Um erro inesperado aconteceu {error}')


#  Menu Interativo da agenda - Inicio do Programa
carregar_agenda()
while True:
    imprimir_menu()

    opcao = input('Opção Desejada: ')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Busca: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Adicionar Contato: ')
        x = contato.capitalize()
        try:
            AGENDA[x]
            print(f'***************************************'
                  f'\nErro, {x} já está registrado na agenda!')
        except KeyError:
            tel, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, tel, email, endereco)
    elif opcao == '4':
        contato = input('Editar Contato: ')
        x = contato.capitalize()
        try:
            AGENDA[x]
            print(f'Editando contato:{x}')
            tel, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, tel, email, endereco)
        except KeyError:
            print(f'Erro: {contato} não está registrado na agenda!')
    elif opcao == '5':
        contato = input('Excluir Contato:')
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo:')
        exportar_contatos(f'{nome_do_arquivo}.csv')
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo:')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('Agenda Encerrada!')
        break
    else:
        print('Opção Inválida!')
