# Menu com as opções de operação do banco
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis iniciais
saldo = 0  # Saldo do cliente
limite = 500  # Limite para saque
extrato = ""  # Extrato de movimentações
numero_saques = 0  # Número de saques realizados
LIMITE_SAQUES = 3  # Limite máximo de saques permitidos

# Loop principal que executa até o usuário escolher sair
while True:
    # Exibe o menu e recebe a opção do usuário
    opcao = input(menu)

    # Opção de depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        # Verifica se o valor do depósito é válido (maior que 0)
        if valor > 0:
            saldo += valor  # Atualiza o saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Adiciona a movimentação ao extrato

        else:
            print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro

    # Opção de saque
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        # Verifica se o saque excede o saldo, o limite ou o número máximo de saques
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        # Se o saque não for permitido por algum motivo, exibe a mensagem correspondente
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        # Se o saque for válido (maior que 0), realiza a operação
        elif valor > 0:
            saldo -= valor  # Atualiza o saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona o saque ao extrato
            numero_saques += 1  # Incrementa o número de saques realizados

        else:
            print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro

    # Opção de exibir o extrato
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        # Se não houver movimentações, exibe uma mensagem informando
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual
        print("==========================================")

    # Opção de sair do programa
    elif opcao == "q":
        break  # Encerra o loop e o programa

    # Caso o usuário digite uma opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
