import time
import os

os.system('cls')

def print_menu():
    print("*------Menu principal------* \n \
      \t[1] - Sacar \n \
      \t[2] - Depositar \n \
      \t[3] - Visualizar Extrato \n \
      \t[4] - Criar Usuário \n \
      \t[5] - Criar Conta \n \
      \t[6] - Listar Contas \n \
      \t[0] - Sair \n*--------------------------*")
    
#OPERAÇÕES
def limpa_terminal(*args):
    os.system('cls')
    print(args[0]) if len(args) > 0 else None

def espera(delayed = 2): time.sleep(delayed)

def extrato(info, valor, extrato_log): extrato_log.append(f"{info}{valor}")

def print_extrato(extrato_log, saldo):
    print("Extrato de conta:")
    for i in extrato_log:
        print(f"\t{i}")
    print(f"\n\t\tSaldo atual: R$ {saldo:.2f}")

def saque(*, saldo, valor_saque, extrato_log, limite_vezes, saque_max):
    if valida_saque(valor_saque, saque_max, limite_vezes, saldo) == 0:
        saldo = atualiza_saque(saldo, valor_saque, saque_max, limite_vezes)
        extrato_log.append(f"Saque: R$ {valor_saque}")
        limpa_terminal("Saque realizado com sucesso!")
        return saldo, extrato_log
    else:
        limpa_terminal("Operação Falhou: Verifique os valores informados!")
        return saldo, limite_vezes

def atualiza_saque(saldo, valor_saque, saque_max, limite_vezes):
    saldo -= valor_saque
    saque_max -= valor_saque
    limite_vezes -= 1
    return saldo

# VALIDAÇÕES SAQUE
def valida_saque(valor_saque, saque_max, limite_vezes, saldo):
    if valor_saque <= 0: limpa_terminal("Operação Falhou: O valor precisa ser positivo!")
    elif valor_saque > saldo: limpa_terminal("Operação Falhou: Saldo insuficiente!")
    elif valor_saque > saque_max: limpa_terminal("Operação Falhou: Valor de saque excede o limite diário!")
    elif limite_vezes == 0: limpa_terminal("Operação Falhou: Limite de saques diários atingido!")
    else: return 0
    return 1

#DEPOSITO
def deposito(valor, saldo, extrato_log, /):
    if deposito_valido(valor, saldo) == 1:
        extrato_log.append(f"Depósito: R$ {valor}")
        valores = atualiza_deposito(saldo, valor), extrato_log
        return valores

    else:
        limpa_terminal("Operação Falhou: Valor por depósito precisa ser positivo!")
        return saldo

def atualiza_deposito(saldo, valor_para_deposito):
    saldo += valor_para_deposito
    limpa_terminal('Valor depositado com sucesso!')
    return saldo
    
# VALIDAÇÕES DEPOSITO
def deposito_valido(valor_para_deposito, saldo):
    if valor_para_deposito > 0: return 1
    elif valor_para_deposito <= 0: return 0

#USUARIO
def criar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    if existe_usuario(cpf, usuarios):
        limpa_terminal("Usuário já cadastrado!")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento: (dd/mm/aaaa) ")
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento})
    limpa_terminal("Cadastro realizado com sucesso!")

# VALIDAÇÕES USUARIO
def existe_usuario(cpf, usuarios):
    for user in usuarios: 
        if user['cpf'] == cpf: return user
    return 0

def criar_conta(agencia, numero_conta, usuarios): 
    cpf = input("Digite o CPF do usuário: ")
    usuario = existe_usuario(cpf, usuarios)

    if usuario:
        agencia = input("Digite a agência: ")
        numero_conta = input("Digite o número da conta: ")
        limpa_terminal("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        limpa_terminal("Usuário não encontrado!")

def main():
    saque_maximo_dia=1500
    LIMITE_VEZES_SAQUE = 3
    AGENCIA = "0001"
    saldo = 150
    extrato_log = []
    usuarios = []
    contas = []

    while True:
        print_menu()
        operacao = int(input("Digite a opção desejada: "))

        if operacao == 1:
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato_log = saque(saldo=saldo, valor_saque=valor, extrato_log=extrato_log, limite_vezes=LIMITE_VEZES_SAQUE, saque_max=saque_maximo_dia)

        elif operacao == 2:
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato_log = deposito(valor, saldo, extrato_log)

        elif operacao == 3:
            print_extrato(extrato_log, saldo)
        
        elif operacao == 4:
            criar_usuario(usuarios)
        
        elif operacao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            contas.append(conta) if conta else None

        
        elif operacao == 6:
            limpa_terminal("Listagem de contas:")
            if len(contas) == 0:
                limpa_terminal("Nenhuma conta cadastrada!")
            else:
                for conta in contas:
                    print(f"\tAgência: {conta['agencia']}\n\tConta: {conta['numero_conta']}\n\tNome: {conta['usuario']['nome']}\n\tCPF: {conta['usuario']['cpf']}\n\tData de Nascimento: {conta['usuario']['data_nascimento']}\n")
                    print(f"Ag/Número: {conta['agencia']}/{conta['numero_conta']}\n")
            espera(5)


        elif operacao == 0:
            print("Saindo do sistema")
            limpa_terminal("Saindo do sistema, até logo!")
            espera()
            limpa_terminal()
            break

        espera()
        limpa_terminal()


main()