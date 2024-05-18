# OBJETIVO GERAL
# SEPARAR AS FUNÇÕES EXISTENTES DE SAQUE, DEPÓSITO E EXTRATO EM FUNÇÕES. CRIAR DUAS NOVAS FUNÇÕES: CADASTRAR USUÁRIO (CLIENTE) E CADASTRAR CONTA BANCÁRIA.

# DESAFIO
# PRECISAMOS DEIXAR NOSSO CÓDIGO MAIS MODULARIZADO, PARA ISSO VAMOS CRIAR FUNÇÕES PARA AS OPERAÇÕES EXISTENTES: SACAR, DEPOSITAR E EXTRATO. ALÉM DISSO, PARA A VERSÃO 2 DO NOSSO SISTEMA PRECISAMOS CRIAR DUAS NOVAS FUNÇÕES: CRIAR USUÁRI(CLIENTE DO BANCO)E CRIAR CONTA CORRENTE (VINCULAR COM USUÁRIO).

# SEPARAÇÃO EM FUNÇÕES
# DEVEMOS CRIAR FUNÇÕES PARA TODAS AS OPERAÇÕES DO SISTEMA. PARA EXERCITAR TUDO O QUE APRENDEMOS NESTE MÓDULO, CADA FUNÇÃO VAI TER UMA REGRA NA PASSAGEM DE ARGUMENTOS. O RETORNO E A FORMA COMO SERÃO CHAMADAS, PODE SER DEFINIDA POR VOCÊ DA FORMA QUE ACHAR MELHOR.

# SAQUE
# A FUNÇÃO SAQUE DEVE RECEBER OS VALORES APENAS POR NOME(KEYWORD ONLY). SUGESTÃO DE ARGUMENTOS: SALDO, VALOR, EXTRATO, LIMITE, NUMERO_SAQUES, LIMITE_SAQUES. SUGESTÃO DE RETORNO: SALDO E EXTRATO.

# DEPÓSITO
# A FUNÇÃO DEPÓSITO DEVE RECEBER OS ARGUMENTOS APENAS POR POSIÇÃO (POSITIONAL ONLY). SUGESTÃO DE ARGUMENTOS: SALDO,VALOR,EXTRATO.SUGESTÃO DE RETORNO:SALDO E EXTRATO.

# EXTRATO
# A FUNÇÃO EXTRATO DEVE RECEBER OS ARGUMENTOS POR POSIÇÃO E NOME (POSITIONAL ONLY E KEYWORD ONLY). ARGUMENTOS POSICIONAIS: SALDO, ARGUMENTOS NOMEADOS: EXTRATO.

# NOVAS FUNÇÕES
# PRECISAMOS CRIAR DUAS NOVAS FUNÇÕES: CRIAR USUÁRIO E CRIAR CONTA CORRENTE. FIQUE A VONTADE PARA ADICIONAR MAIS FUNÇÕES, EXEMPLO: LISTAR CONTAS

# CRIAR USUÁRIO(CLIENTE)
# O PROGRAMA DEVE ARMAZENAR OS USUÁRIOS EM UMA LISTA, UM USUÁRIO É COMPOSTO POR: NOME, DATA DE NASCIMENTO,CPF E ENDEREÇO. O ENDEREÇO É UMA STRING COM O FORMATO: LOGRADOURO, NRO - BAIRRO - CIDADE/SIGLA ESTADO. DEVE SER ARMAZENADO SOMENTE OS NUMEROS DO CPF. NÃO PODEMOS CADASTRAR 2 USUÁRIOS COM O MESMO CPF.

# CRIAR CONTA CORRENTE
# O PROGRAMA DEVE ARMAZENAR CONTAS EM UMA LISTA, UMA CONTA É COMPOSTA POR: AGÊNCIA, NÚMERO DA CONTA E USUÁRIO. O NÚMERO DA CONTA É SEQUENCIAL, INICIANDO EM 1. 0 NUMERO DA AGÊNCIA É FIXO: '0001'. O USUÁRIO PODE TER MAIS DE UMA CONTA, MAS UMA CONTA PERTENCE A SOMENTE UM USUÁRIO. AO CRIAR A CONTA TEM QUE SER VINCULADA A UM USUÁRIO

# DICA
# PARA VINCULAR UM USUÁRIO A UMA CONTA, FILTRE A LISTA DE USUÁRIOS BUSCANDO O NÚMERO DO CPF INFORMADO PARA CADA USUÁRIO DA LISTA. 

def menu():
    menu = """\n
    ------------BEM-VINDO------------
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [nc] - Nova conta
    [lc] - Listar contas
    [nu] - Novo usuário
    [q] - Sair
    => """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print('digite um valor valido!')
    else:
        saldo += valor
        extrato += (f'depósito: R${valor:.2f}\n')
        print('depósito realizado com sucesso!')

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print(f'saldo insuficiente!\nseu saldo atual é de:{saldo}')

    elif valor > limite:
        print('valor acima do limite!\n seu limite atual é de: R$500.00')

    elif numero_saques >= limite_saques:
        print('limite de saques atingido!')

    elif valor > 0:
        saldo -= valor
        extrato += (f'Saque: R$ {valor:.2f}\n')
        numero_saques += 1
        print('saque realizado!')

    else:
        print('valor invalido!')

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    
    print('sem movimentações!' if not extrato else extrato)
    print(f"\nSaldo:R$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('usuario com esse cpf já existe!')
        return

    nome = input('informe o nome completo: ')
    data_nascimento = input('informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print('usuário criado')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('informe o cpf:')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('conta criada!')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print('usuario não encontrado!')


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
