nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()

while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NAO":
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
    doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()


if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para sala AMARELA")
else:
    print("Encaminhe o paciente para sala BRANCA")


if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero = input("Digite o gênero do paciente: ").upper()
    while genero != "FEMININO" and genero != "MASCULINO":
        print("Responda o seu gênero com MASCULINO ou FEMININO")
        genero = input("Digite o gênero do paciente: ").upper()
    if genero == "FEMININO" and idade>10:
        gravidez = input("A paciente está grávida? ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")