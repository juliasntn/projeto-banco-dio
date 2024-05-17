# Banco Digital - Desafio Dio.me

Este repositório contém a solução para um desafio de programação proposto pela plataforma [Dio.me](https://www.dio.me/). O objetivo do desafio é implementar um menu de operações bancárias em Python, permitindo que o usuário realize depósitos, saques, consulte o extrato e saia do programa.

## Funcionalidades

O programa oferece as seguintes funcionalidades:

- **Depósito**: Permite ao usuário depositar uma quantia na conta.
- **Saque**: Permite ao usuário sacar uma quantia da conta, respeitando o limite de valor e a quantidade de saques permitidos.
- **Extrato**: Exibe todas as movimentações (depósitos e saques) realizadas na conta.
- **Sair**: Encerra a execução do programa.

## Regras de Negócio

1. **Depósito**: O valor do depósito é adicionado ao saldo da conta e registrado no extrato.
2. **Saque**: 
    - O valor do saque não pode ser superior a R$500,00.
    - O usuário pode realizar no máximo 3 saques por dia.
    - O saldo deve ser suficiente para cobrir o valor do saque.
3. **Extrato**: Exibe todas as transações realizadas. Caso não haja movimentações, exibe a mensagem "Sem movimentações."
4. **Sair**: Encerra o programa.

## Código

```python
menu = '''
[d] = depositar
[s] = saque
[e] = extrato
[q] = exit

=>'''

# Variáveis
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    # Seleciona a opção
    opcao = input(menu)
    print("----------------------------------")

    # Condicional para as funções do programa
    if opcao == 'd':
        print('Você escolheu a opção depositar!')
        print('-------------------')
        # Escolhe o valor a ser depositado
        deposito = float(input('Quanto você deseja depositar:'))
        # Adiciona o valor ao saldo
        saldo += deposito
        # Adiciona ao extrato
        extrato += (f'Depósito = R${deposito:.2f}\n')
        print(f'Seu saldo atual é: R${saldo:.2f}')
    elif opcao == 's':
        print('Você escolheu a opção saque!')
        print('-------------------')
        # Escolhe o valor a ser sacado
        saque = float(input('Quanto você deseja sacar:'))
        # Condição para impedir que seja feito mais de 3 saques
        if numero_saques >= LIMITE_SAQUES:
            print('Você atingiu o número máximo de saques!')
        else:
            # Condição para impedir que seja feito um saque maior que 500
            if saque > 500:
                print('Você escolheu um valor acima do permitido!\nO seu limite atual é de R$500,00')
            else:
                # Condição para caso não tenha saldo suficiente
                if saldo < saque:
                    print(f'Você não tem saldo suficiente, seu saldo atual é: R${saldo:.2f}')
                else:
                    print(f'Saque no valor de R${saque:.2f} efetuado com sucesso!')
                    # Adiciona ao extrato
                    extrato += (f'Saque = -R${saque:.2f}\n')
                    # Retira o valor sacado do saldo
                    saldo -= saque
                    # Adiciona 1 saque ao número de saques
                    numero_saques += 1
    elif opcao == 'e':
        print('Você escolheu a opção extrato!')
        print('-------------------')
        print("Sem movimentações." if not extrato else extrato)
        print(f'Seu saldo atual é de: R${saldo:.2f}')
    elif opcao == 'q':
        print('Você escolheu sair!\nVolte sempre!!!')
        break
    else:
        print('Opção inválida!\nPor favor tente novamente!')
```

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou copie o código acima para um arquivo local.
3. Execute o arquivo Python no terminal ou em um ambiente de desenvolvimento integrado (IDE).

```bash
python nome_do_arquivo.py
```



Divirta-se codificando! 🚀
