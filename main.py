import time
import os

saque_maximo_dia=1500
limite_vezes_saque = 3
saldo = 0
extrato = []

os.system('cls')

menu = "*------Menu principal------* \n \
      \t1 - Sacar \n \
      \t2 - Depositar \n \
      \t3 - Visualizar Extrato \n \
      \t0 - Sair \n\
*--------------------------*"


while True:
    print(menu)

    opcao = input("Digite a opção desejada: ")
    os.system('cls')

    if opcao == '1':
        valor_saque = int(input("Digite o valor a ser sacado: "))
        if valor_saque <= 0: print("Operação Falhou: Valor inválido!")
        elif valor_saque > saldo: print("Operação Falhou: Saldo insuficiente!")
        elif valor_saque > saque_maximo_dia: print("Operação Falhou: Valor de saque excede o limite diário!")
        elif limite_vezes_saque == 0: print("Operação Falhou: Limite de saques diários atingido!")
        else:
            saldo -= valor_saque
            extrato.append(f"Saque: R$ {valor_saque}")
            saque_maximo_dia -= valor_saque
            limite_vezes_saque -= 1
            os.system('cls')
            print("Saque realizado com sucesso!") 

    elif opcao == '2':
        while True:
            valor_depositado = float(input("Digite o valor a ser depositado: "))
            if valor_depositado > 0:
                saldo += valor_depositado
                extrato.append(f"Depósito: R$ {valor_depositado}")
                os.system('cls')
                print('Valor depositado com sucesso!')
                break
                
            elif valor_depositado <= 0:
                os.system('cls')
                print("Operação Falhou: Valor por depósito precisa ser positivo!")
                break



    elif opcao == '3':
        print("Extrato de conta:")
        for i in extrato:
            print(i)
        print(f"\tSaldo atual: R$ {saldo:.2f}")
        time.sleep(2)
    
    elif opcao == '0':
        print("Saindo do sistema")
        break
    else:
        print("Opção inválida")
    
    time.sleep(2)
    #clear screen
    os.system('cls')

