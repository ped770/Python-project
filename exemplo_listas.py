inventario = []
resposta = input("Você deseja fazer um inventário? ").upper()

while resposta == "SIM":
    inventario.append(input("Produto: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número de série: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite 'sim' para continuar: ").upper()

for elemento in inventario:
    print(elemento)