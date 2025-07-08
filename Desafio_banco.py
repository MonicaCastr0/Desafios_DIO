
def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor: .2f} \n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.") 
    return extrato, saldo

def sacar(*, valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Você excedeu o limite de saque diario.")
    elif valor <= saldo:
        saldo -= valor 
        extrato += f"Saque: R$ {valor: .2f} \n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("O valor informado é inválido.")

    return saldo, extrato, numero_saques

def visualizar_extrato(saldo, / , * , extrato):

    print("=============| EXTRATO |=============")
    print("Não foram realizadas movimentações. " if not extrato else extrato)
    print(f"Saldo: R${saldo: .2f} \n")
    print("=====================================")

def criar_usuario(usuarios):
    cpf = input("Informe o cpf: (Somente os numeros)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já esta cadastrado no sistema.")
        return
    else:
        nome = input("Informe o nome o nome completo: ")
        data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa): ")
        endereco = input("Informe o endereço(logradouro, nro - bairro - cidade/sigla estado): ")
        
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})
        print("Usuário criado com sucesso!.")

def filtrar_usuario(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuario_filtrados[0] if usuario_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta cadastrada com sucesso!.")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    else:
        print("Usuário não encontrado!.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:{conta["agencia"]}
            C/C:{conta["numero_conta"]}
            Titular:{conta["usuario"]["nome"]}
        """
        print(linha) 

def main():

    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0 
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    numero_conta = 0
    AGENCIA = "0001"

    while True:
        opcao = int(input("""
        #################| SISTEMA BANCÁRIO |##########################  
                        
            Digite a Operação que você deseja realizar:
            1.Depósito.
            2.Saque.
            3.Extrato.
            4.Sair. 
            5.Novo usuário.
            6.Nova Conta.  
            7.Contas cadastradas.      
            """))
        if opcao == 4:
            print("Obrigado por utilizar os nossos serviços.")
            break
        elif opcao == 1:
            valor = float(input("Digite o valor do deposito: "))
            extrato, saldo = depositar(valor, saldo, extrato)
        
        elif opcao == 2:
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = sacar(valor=valor,saldo=saldo,extrato=extrato,limite=limite,numero_saques=numero_saques,LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == 3:
            visualizar_extrato(saldo, extrato=extrato)

        elif opcao == 5:
            criar_usuario(usuarios)
             
        elif opcao == 6:
            numero_conta = numero_conta + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == 7:
            listar_contas(contas)

        else:
            print("Opção inválida.")


main()