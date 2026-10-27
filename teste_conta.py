from cliente import ContaBancaria


# TESTE 01 - Criar conta com dados válidos
print("\nTESTE 01 - Criar conta")

conta1 = ContaBancaria("001", "Ana Lima")

print("Número:", conta1.numero)
print("Titular:", conta1.titular)
print("Saldo inicial:", conta1.get_saldo())
print("Esperado: 0.0")


# TESTE 02 - Criar conta com titular muito curto
print("\nTESTE 02 - Titular com menos de 3 caracteres")

try:
    conta1 = ContaBancaria("001", "Al")
    print("FALHOU: aceitou um titular inválido.")
except ValueError as erro:
    print("Erro esperado:", erro)


# TESTE 03 - Depositar 100
print("\nTESTE 03 - Depositar 100")

conta1 = ContaBancaria("001", "Ana Lima")
conta1.depositar(100)

print("Saldo após depósito:", conta1.get_saldo())
print("Esperado: 100.0")


# TESTE 04 - Depositar zero
print("\nTESTE 04 - Depositar zero")

conta1 = ContaBancaria("001", "Ana Lima")
conta1.depositar(100)

try:
    conta1.depositar(0)
    print("FALHOU: aceitou depósito de zero.")
except ValueError as erro:
    print("Erro esperado:", erro)

print("Saldo final:", conta1.get_saldo())
print("Esperado: 100.0, sem alteração")


# TESTE 05 - Depositar valor negativo
print("\nTESTE 05 - Depositar -50")

conta1 = ContaBancaria("001", "Ana Lima")
conta1.depositar(100)

try:
    conta1.depositar(-50)
    print("FALHOU: aceitou depósito negativo.")
except ValueError as erro:
    print("Erro esperado:", erro)

print("Saldo final:", conta1.get_saldo())
print("Esperado: 100.0, sem alteração")


# TESTE 06 - Sacar 40 de um saldo de 100
print("\nTESTE 06 - Sacar 40")

conta1 = ContaBancaria("001", "Ana Lima")
conta1.depositar(100)
conta1.sacar(40)

print("Saldo após saque:", conta1.get_saldo())
print("Esperado: 60.0")


# TESTE 07 - Sacar todo o saldo
print("\nTESTE 07 - Sacar 100 de um saldo de 100")

conta1 = ContaBancaria("001", "Ana Lima")
conta1.depositar(100)
conta1.sacar(100)

print("Saldo após saque:", conta1.get_saldo())
print("Esperado: 0.0")


# TESTE 08 - Sacar mais do que o saldo disponível
print("\nTESTE 08 - Sacar 100.01 de um saldo de 100")

conta1 = ContaBancaria("001", "Ana Lima")
conta1.depositar(100)

try:
    conta1.sacar(100.01)
    print("FALHOU: aceitou saque maior que o saldo.")
except ValueError as erro:
    print("Erro esperado:", erro)

print("Saldo final:", conta1.get_saldo())
print("Esperado: 100.0, sem alteração")


# TESTE 09 - Transferir 30
print("\nTESTE 09 - Transferir 30")

conta1 = ContaBancaria("001", "Ana Lima")
conta2 = ContaBancaria("002", "Carlos Souza")

conta1.depositar(100)
conta1.transferir(conta2, 30)

print("Saldo de Ana:", conta1.get_saldo())
print("Esperado: 70.0")

print("Saldo de Carlos:", conta2.get_saldo())
print("Esperado: 30.0")


# TESTE 10 - Transferir para a própria conta
print("\nTESTE 10 - Transferir para a própria conta")

conta1 = ContaBancaria("001", "Ana Lima")
conta1.depositar(100)

try:
    conta1.transferir(conta1, 30)
    print("FALHOU: aceitou transferência para a própria conta.")
except ValueError as erro:
    print("Erro esperado:", erro)

print("Saldo final:", conta1.get_saldo())
print("Esperado: 100.0, sem alteração")


# TESTE 11 - Criar conta com número vazio
print("\nTESTE 11 - Número vazio")

try:
    conta1 = ContaBancaria("", "Ana Lima")
    print("FALHOU: aceitou número vazio.")
except ValueError as erro:
    print("Erro esperado:", erro)


# TESTE 12 - Criar conta com número nulo
print("\nTESTE 12 - Número nulo")

try:
    conta1 = ContaBancaria(None, "Ana Lima")
    print("FALHOU: aceitou número nulo.")
except ValueError as erro:
    print("Erro esperado:", erro)


# TESTE 13 - Sacar zero
print("\nTESTE 13 - Sacar zero")

conta1 = ContaBancaria("001", "Ana Lima")
conta1.depositar(100)

try:
    conta1.sacar(0)
    print("FALHOU: aceitou saque de zero.")
except ValueError as erro:
    print("Erro esperado:", erro)

print("Saldo final:", conta1.get_saldo())
print("Esperado: 100.0, sem alteração")


# TESTE 14 - Sacar valor negativo
print("\nTESTE 14 - Sacar -20")

conta1 = ContaBancaria("001", "Ana Lima")
conta1.depositar(100)

try:
    conta1.sacar(-20)
    print("FALHOU: aceitou saque negativo.")
except ValueError as erro:
    print("Erro esperado:", erro)

print("Saldo final:", conta1.get_saldo())
print("Esperado: 100.0, sem alteração")


# TESTE 15 - Transferir para destino nulo
print("\nTESTE 15 - Transferir para destino nulo")

conta1 = ContaBancaria("001", "Ana Lima")
conta1.depositar(100)

try:
    conta1.transferir(None, 30)
    print("FALHOU: aceitou destino nulo.")
except ValueError as erro:
    print("Erro esperado:", erro)

print("Saldo final:", conta1.get_saldo())
print("Esperado: 100.0, sem alteração")


# TESTE 16 - Transferir sem saldo suficiente
print("\nTESTE 16 - Transferir 150 com saldo de 100")

conta1 = ContaBancaria("001", "Ana Lima")
conta2 = ContaBancaria("002", "Carlos Souza")

conta1.depositar(100)
conta2.depositar(50)

try:
    conta1.transferir(conta2, 150)
    print("FALHOU: aceitou transferência sem saldo suficiente.")
except ValueError as erro:
    print("Erro esperado:", erro)

print("Saldo de Ana:", conta1.get_saldo())
print("Esperado: 100.0, sem alteração")

print("Saldo de Carlos:", conta2.get_saldo())
print("Esperado: 50.0, sem alteração")


# TESTE 17 - Transferir zero
print("\nTESTE 17 - Transferir zero")

conta1 = ContaBancaria("001", "Ana Lima")
conta2 = ContaBancaria("002", "Carlos Souza")

conta1.depositar(100)
conta2.depositar(50)

try:
    conta1.transferir(conta2, 0)
    print("FALHOU: aceitou transferência de zero.")
except ValueError as erro:
    print("Erro esperado:", erro)

print("Saldo de Ana:", conta1.get_saldo())
print("Esperado: 100.0, sem alteração")

print("Saldo de Carlos:", conta2.get_saldo())
print("Esperado: 50.0, sem alteração")


# TESTE 18 - Transferir valor negativo
print("\nTESTE 18 - Transferir -30")

conta1 = ContaBancaria("001", "Ana Lima")
conta2 = ContaBancaria("002", "Carlos Souza")

conta1.depositar(100)
conta2.depositar(50)

try:
    conta1.transferir(conta2, -30)
    print("FALHOU: aceitou transferência negativa.")
except ValueError as erro:
    print("Erro esperado:", erro)

print("Saldo de Ana:", conta1.get_saldo())
print("Esperado: 100.0, sem alteração")

print("Saldo de Carlos:", conta2.get_saldo())
print("Esperado: 50.0, sem alteração")


print("\nTESTE 19 - Consultar saldo")

conta1 = ContaBancaria("001", "Ana Lima")
conta1.depositar(100)

print("Primeira consulta:", conta1.get_saldo())
print("Segunda consulta:", conta1.get_saldo())
print("Esperado: 100.0 nas duas consultas")