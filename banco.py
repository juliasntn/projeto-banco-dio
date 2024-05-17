# DESAFIO
# FOMOS CONTRATADOS POR UM GRANDE BANCO PARA DESENVOLVER O SEU NOVO SISTEMA. ESSE BANCO DESEJA MODERNIZAR SUAS OPERAÇÕES E PRA ISSO ESCOLHEU A LINGUAGEM PYTHON. PARA A PRIMEIRA VERSÃO DO SISTEMA DEVEMOS IMPLEMENTAR APENAS 3 OPERAÇÕES: DEPÓSITO, SAQUE E EXTRATO.

# OPERAÇÃO DE DEPÓSITO
# DEVE SER POSSÍVEL DEPOSITAR VALORES PARA A MINHA CONTA BANCÁRIA. A V1 DO PROJETO TRABALHA APENAS COM 1 USUÁRIO, DESSA FORMA NÃO PRECISMOS NOS PREOCUPAR EM IDENTIFICAR QUAL É O NUMERO DA AGÊNCIA E CONTA BANCÁRIA. TODOS OS DESPÓSITOS DEVEM SER ARMAZENADOS EM UMA VARIÁVEL E EXIBIDOS NA OPERAÇÃO DE EXTRATO.

# OPERAÇÃO DE SAQUE
# O SISTEMA DEVE PERMITIR REALIZAR 3 SAQUES DIÁRIOS COM LIMITE MÁXIMO DE R$500,00 POR SAQUE. CASOO USUÁRIO NÃO TENHA SALDO EM CONTA, O SISTEMA DEVE EXIBIR UMA MENSAGEM INFORMANDO QUE NÃO SERÁ POSSÍVEL SACAR O DINHEIRO POR FALTA DE SALDO. TODOS OS SAQUES DEVEM SER ARMAZENADOS EM UMA VARIÁVEL E EXIBIDOS NA OPERAÇÃO DE EXTRATO.

# OPERAÇÃO DE EXTRATO
# ESSA OPERAÇÃO DEVE LISTAR TODOS OS DEPÓSITOS E SAQUES REALIZADOS NA CONTA. NO FIM DA LISTAGEM DEVE SER EXIBIDO O SALDO ATUAL DA CONTA. OS VALORES DEVEM SER EXIBIDOS UTILIZANDO O FORMATO R$xxx.xx, EXEMPLO: 1500.45 = R$ 1500.45


# menu do meu banco
menu = '''
[d] = depositar
[s] = saque
[e] = extrato
[q] = exit

=>'''

# variaveis
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    # seleciona a opção
    opcao = input(menu)
    print("----------------------------------")

    # condicional para as funções do programa
    if(opcao == 'd'):
        print('Você escolheu a opção depositar!')
        print('-------------------')
        # escolhe o valor a ser depositado
        deposito = float(input('Quanto você deseja depositar:'))
        # adiciona o valor ao saldo
        saldo += deposito
        # faz adição ao extrato
        extrato += (f'Deposito = R${deposito:.2f}\n')
        print(f'seu saldo atual é: {saldo}')
    elif(opcao == 's'):
        print('Você escolheu a opção saque!')
        print('-------------------')
        # escolhe o valor que desejesa ser sacado
        saque = float(input('Quanto você deseja sacar:'))
        # condição para impedir que seja feito mais de 3 saques
        if(numero_saques >= LIMITE_SAQUES):
            print('Você atingiu o número máximo de saques!')
        else:
            # condição para impedir que seja feito um saque maior que 500
            if(saque > 500):
                print('Você escolheu um valor acima do permitido!\nO seu limite atual e de R$500.00')
            else:
                # condição para caso não tenha saldo suficiente
                if(saldo < saque):
                    print(f'Você não tem saldo suficiente, seu saldo atual é:{saldo}')
                else:
                    print(f'Saque no valor de {saque} efetuado com sucesso!')
                    # adiciona ao extrato
                    extrato += (f'Saque = -R${saque:.2f}\n')
                    # retira o valor sacado do saldo
                    saldo -= saque
                    # adiciona 1 saque ao numero de saques
                    numero_saques +=1

    elif(opcao == 'e'):
        print('Você escolheu a opcção extrato!')
        print('-------------------')
        print("Sem movimentações." if not extrato else extrato)
        print(f'Seu saldo atual é de:R${saldo:.2f}')
    
    elif(opcao == 'q'):
        print('Você escolheu sair!\nVolte sempre!!!')
        break
    else:
        print('Opção invalida!\nPor favor tente novamente!')
    