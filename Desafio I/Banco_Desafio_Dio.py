menu = """ 
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Escolha uma das opções: 
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input(f'Qual o valor do deposito? '))
        if valor > 0:
            saldo += valor
            extrato += f'\nVocê depositou: R$ {valor:.2f}\n'
            print(extrato)
        else:
            print('Erro na operação! Valor incorreto')
    elif opcao == "2":
        valor = float(input(f'Qual o valor do saque?'))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

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
        else:
            print('O valor informado é inválido.')

    elif opcao == '3':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == '4':
        break

    else:
        print('Opção Invalida')

