from datetime import datetime, time

# Menu de opcões
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
 
=> """

# Variáveis
data_completa = datetime.now().strftime("%d/%m/%Y")
data_atual = datetime.now().strftime("%d/%m")
deposito = 0
saldo = 0
limite = 500
extrato = f"""
            BANCO JR S.A.         
{data_completa} AUTOATENDIMENTO        
        EXTRATO DE MOVIMENTAÇÃO    
AGÊNCIA:           CONTA:          
CLIENTE:                             
                                     
DATA    HISTÓRICO           VALOR  
"""
numero_saques = 0
LIMITE_SAQUES = 3
depositos = []
saques = []

# Condicionais
while True:
    opcao = input(menu)

    # Condições para depósito
    if opcao == "d":

        # Verificando se a entrada é númeral
        while True:
            valor_deposito = input("Digite o valor do depósito R$ ").replace(",", '.')
            try:
                deposito = float(valor_deposito)
                if deposito < 50:
                    print("Valor mínimo para depósito é de R$ 50,00!")
                else:
                    saldo += deposito
                    depositos.append(deposito)
                    print("...")
                    time.sleep(1)
                    print(f"Depósito efetuado com sucesso")
                    print(f"O valor do saldo atual é de R$ {saldo:.2f}")
                    break
            except ValueError:
                print("Não é um número, valor inválido")

    # Condições para saque
    elif opcao == "s":
        if LIMITE_SAQUES == 0:
            print("Você atingiu o limite máximo de saques por dia")
        elif saldo > 0:

            # Verificando se a entrada é númeral
            while True:
                valor_saque = input("Digite o valor do saque R$ ").replace(",", ".")
                try:
                    saque = float(valor_saque)
                    if saque > limite:
                        print("Valor máximo para saque é de R$ 500,00!")
                    elif saque > saldo:
                        print("Saldo insuficiente para saque!")
                    else:
                        saldo -= saque
                        saques.append(saque)
                        numero_saques += 1
                        LIMITE_SAQUES -= 1
                        print("...")
                        time.sleep(1)
                        print(f"Saque efetuado com sucesso")
                        print(f"O valor do saldo atual é de R$ {saldo:.2f}")
                        print(f"Numero de saques: {numero_saques}")
                        break
                except ValueError:
                    print("Valor inválido")
        else:
            print("Não é possível efetuar a operação no momento, faça um depósito!!")

    # Condições para extrato
    elif opcao == "e":
        print("-=" * 19)
        print(extrato)
        for valor in depositos:
            print(f"{data_atual}\tDepósito\t\t\t{valor:.2f}")
        for saque in saques:
            print(f"{data_atual}\tSaque\t\t\t\t{saque:.2f}")

        print(f"{data_atual}\tSaldo atual\t\t\t{saldo:.2f}\n")
        print("-=" * 19)

    # Sair do Sistema
    elif opcao == "q":
        print("Obrigado por usar nosso sistema!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
