
saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:
    opcao = int(input("""
    #################| SISTEMA BANCÁRIO |##########################  
                      
        Digite a Operação que você deseja realizar:
           ir:
"""))
    if opcao == 4:
        print("Obrigado por utilizar os nossos serviços")
        break
    elif opcao == 1:
        valor = float(input("Digite o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f} \n"
        else:
            print("Operação falhou! O valor informado é inválido") 
    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente: ")
        elif valor > limite:
            print("O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Você excedeu o limite de saque diario.")
        elif valor <= saldo:
            saldo -= valor 
            extrato += f"Saque: R$ {valor: .2f} \n"
            numero_saques += 1
        else:
            print("O valor informado é inválido.")
    elif opcao == 3:
        print("=============| EXTRATO |=============")
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"Saldo: R${saldo: .2f} \n")
        print("=====================================")
    else:
        print("Opção inválida.")