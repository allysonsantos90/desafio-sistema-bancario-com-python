import textwrap
def menu ():
        menu = """ 
                MENU
        
        Escolha uma das opções: 
        
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Criar Usuario
        [5] Criar Conta Corrente
        [6] Listar Contas
        [0] Sair
        
        Opção:   
            """
        return input(textwrap.dedent(menu))
def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'\nVocê depositou: R$ {valor:.2f}\n'
        print(extrato)
        print(f'Depósito reazalizado com sucesso!')
    else:
        print('Erro na operação! Valor incorreto')
    return saldo, extrato

def saque (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('Saldo insuficiente.')
        print(f'Seu saldo é : {saldo}')

    elif excedeu_limite:
        print('O valor do saque excede o limite.')

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print(f'Seu saldo é : {saldo}')
        numero_saques += 1
        print(" Saque realizado com sucesso!")

    else:
        print('O valor informado é inválido.')

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def novo_usuario(usuarios):
    cpf = int(('Informe seu CPF (somento numeros): '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Ja Existe usario com esse CPF!')
        return
    nome = input('Informe o nome completo:')
    data_nascimento = input('Iforme a data de nascimento(dd-mm-aaaa): ')
    endereco = input('Informe seu endereço (rua, numero - bairro - cidade/estado: ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuário criado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf ]
    return usuarios_filtrados [0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('Conta Criada com sucesso!')
        return {'agencia': agencia, 'numero)conta': numero_conta, 'usuario': usuario}

    print('Usuario não encontrado!')

def listar_contas(contas):
    for conta in contas:
        linha = f'''Agência:\t{conta['agencia']}
                C/C: {conta['numero_conta']}
                Titular:{conta['usuario']['nome']}
        '''
        print('='* 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios =[]
    contas = []


    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input(f'Qual o valor do deposito? '))

            saldo, extrato = depositar(saldo,valor,extrato)

        elif opcao == "2":
            valor = float(input(f'Qual o valor do saque?'))

            saldo, extrato, saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            novo_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '6':
            listar_contas(contas)

        elif opcao == '0':
            break

        else:
            print('Opção Invalida,  por favor selecione novamente a operação desejada.')


main()

