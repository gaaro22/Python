menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

Selecione uma das opções: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor para depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! Valor informado inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor para saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Você ultrapassou o limite de saque.")
        elif excedeu_saques:
            print("Operação falhou! Você já realizou seus três saques diários.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! informe um valor válido.")

    elif opcao == "3":
        print("========== EXTRATO BANCARIO ==========")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("======================================")

    elif opcao == "4":
        break

    else:
        print("Digite uma opção válida!")

