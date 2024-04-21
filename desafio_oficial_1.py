saldo = 0
limite = 500
extrato_deposito = []
extrato_saque = []
numero_de_saques = 0
LIMITE_DE_SAQUES = 3


while True:
    
    menu = input('''

    Digite uma das opções abaixo:

[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

''')

    if menu.lower() == 'd':
        valor_do_deposito = float(input('\nDigite o valor que você quer depositar no banco: '))
        if valor_do_deposito > 0:
            saldo += valor_do_deposito
            valor_do_deposito = f'R${valor_do_deposito:.2f}'
            extrato_deposito.append(valor_do_deposito)
            print('O valor do depósito foi de:', valor_do_deposito)
            print(f'\nSaldo: R$ {saldo:.2f}')
        else:
             print('Valor inválido! Tente novamente.')

    elif menu.lower() == 's':
        valor_do_saque = float(input('\nDigite o valor que você deseja sacar: '))

        if valor_do_saque > saldo:
             print('Saldo insuficente! Tente novamente com um valor menor.')
        
        elif valor_do_saque > limite:
             print('Limite insuficiente! Tente novamente com um valor menor.')
        
        elif numero_de_saques >= LIMITE_DE_SAQUES:
             print('Não é possivel fazer o saque. Limite disponivel esgotado.')

        else:
             saldo -= valor_do_saque
             numero_de_saques += 1
             valor_do_saque = f'R${valor_do_saque:.2f}'
             extrato_saque.append(valor_do_saque)
             print('O valor do saque foi de:', valor_do_saque)
             print(f'\nSaldo: R$ {saldo:.2f}')
    
    elif menu.lower() == 'e':
        if extrato_deposito:
            print('\nSeus depósitos foram de: ', extrato_deposito)
        
        else:
            print('\nNão foram realizados depósitos na conta.')
        
        if extrato_saque:
            print('\nSeus saques foram de: ', extrato_saque, 'totalizando', numero_de_saques, 'saques.')
        
        else:
            print('\nNão foram realizados saques na conta.')

        print(f'\nSaldo: R$ {saldo:.2f}')

    elif menu.lower() == 'q':
        break

    else:
        print('\nOperação inválida, por favof selecione novamente a operação desejada.')