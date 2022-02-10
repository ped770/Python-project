nome = input("Digite o seu nome: ")
turma = input("Digite sua turma: ")
n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
n3 = float(input("Digite a sua terceira nota: "))
n4 = float(input("Digite a sua quarta nota: "))

media = float((n1 + n2 + n3 + n4) / 4)

if media >= 6:
    print("O aluno(a)", nome, "da turma", turma, "foi aprovado(a) com a média " + str(media))
else:
    print("O aluno(a)", nome, "da turma", turma, "foi reprovado(a) com a média " + str(media))