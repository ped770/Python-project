equipamentos = []
valores = []
serial = []
departamentos = []

resposta = input("Você quer montar uma lista? ").upper()
while resposta == "SIM":
    print("\n")
    equipamentos.append(input("Qual o nome? "))
    valores.append(float(input("Qual o valor? ")))
    serial.append(int(input("Qual o número de série? ")))
    departamentos.append(input("Qual o departamento? "))
    resposta = input("Você quer continuar? ").upper()

for indice in range(0, len(equipamentos)):
    print("\n")
    print("Equipamento...: ", (indice + 1))
    print("Nome.........:", equipamentos[indice])
    print("Valor.........:", valores[indice])
    print("Serial.........:", serial[indice])
    print("Departamento.........:", departamentos[indice])

busca = input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
    if busca == equipamentos:
        print("Valor...: ", valores[indice])
        print("Serial...:", serial[indice])