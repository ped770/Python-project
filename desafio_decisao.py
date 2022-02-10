nivel = input("Qual o seu nível? ").upper()
genero = input("Qual o seu gênero? ").upper()

if nivel == "ADM":
    if genero == "FEMININO":
        print("Olá administradora")
    else:
        print("Olá administrador")

elif nivel == "USR":
    if genero == "FEMININO":
        print("Olá usuária")
    else:
        print("Olá usuário")

elif nivel == "GUEST":
    print("Olá visiante")

else:
    print("Olá desconhecido(a)")