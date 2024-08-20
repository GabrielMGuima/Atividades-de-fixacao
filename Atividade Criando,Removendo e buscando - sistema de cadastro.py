import textwrap

def menu():
    menu = """\n
----------- MENU ----------
[1] \tAdicionar Cliente
[2] \tExibir Clientes
[3] \tBuscar Cliente por E-mail
[4] \tRemover Cliente
[0] \tSair
=> """
    return input(textwrap.dedent(menu))

def adicionar_cliente(clientes):
    nome = input('Informe o Nome: ')
    email = input('Informe o E-mail: ')
    telefone = input('Informe o Telefone: ')
    endereco = input('Informe o Endereço: ')
    
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)
    print('Cliente adicionado com sucesso!')

def exibir_clientes(clientes):
    if not clientes:
        print('Nenhum cliente cadastrado.')
    else:
        for cliente in clientes:
            print(f'Nome: {cliente[0]}, E-mail: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}')

def buscar_cliente(clientes, email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f'Nome: {cliente[0]}, E-mail: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}')
            return
    print('Cliente não encontrado.')

def remover_cliente(clientes, email):
    for cliente in clientes:
        if cliente[1] == email:
            clientes.remove(cliente)
            print('Cliente removido com sucesso!')
            return
    print('Cliente não encontrado.')

def main():
    clientes = []

    while True:
        opcao = menu()
        if opcao == '1':
            adicionar_cliente(clientes)
        elif opcao == '2':
            exibir_clientes(clientes)
        elif opcao == '3':
            email = input('Informe o E-mail do cliente: ')
            buscar_cliente(clientes, email)
        elif opcao == '4':
            email = input('Informe o E-mail do cliente: ')
            remover_cliente(clientes, email)
        elif opcao == '0':
            break
        else:
            print('Operação inválida, por favor selecione novamente a operação desejada.')

main()
