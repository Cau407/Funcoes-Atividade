notas = []

def adicionar_nota():
    nota = float(input("Digite a nota que deseja adicionar: "))
    if nota > 10 or nota < 0:
        print("Você digitou uma nota inválida")
        nota = int(input("Digite a nota que deseja adicionar: "))
    notas.append(nota)
    print(f"Nota {nota} adicionada com sucesso!")

def calcular_media():
    if notas:
        media = sum(notas) / len(notas)
        print(f"A sua média é {media}. Para verificar sua situação, escolha a opção [3]")
        return media
    else:
        print("Nenhuma nota adicionada ainda.")
        return None

def verificar_situacao(media):
    if 0 <= media < 7:
        print("Reprovado")
    elif 7 <= media < 10:
        print("Aprovado")
    elif media == 10:
        print("Parabéns, sua média é 10")
    else:
        print("Parece que houve um problema com as notas que você inseriu, pois a média está como um número inválido, infelizmente você deverá reiniciar o programa e reenserir suas notas, verifique se está digitando corretamente!")

media = None

while True:
    menu = int(input("""
Digite uma opção:
[1] - Adicionar uma nota
[2] - Calcular a média
[3] - Verificar a situação do aluno
[0] - Sair
"""))
    match menu:
        case 1:
            adicionar_nota()
        case 2:
            media = calcular_media()
        case 3:
            if media is None:
                print("Você deve calcular a média antes de verificar a situação")
            else:
                verificar_situacao(media)
        case 0:
            print("Você saiu com sucesso")
            break
        case _:
            print("Você digitou uma opção inválida")