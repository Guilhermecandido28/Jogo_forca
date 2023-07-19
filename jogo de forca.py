from random import randint

def jogar():
    mensagem_bem_vindo()
    palavra_secreta = palavra_chave()
    lista = inicio_forca(palavra_secreta)
    erros = dificuldade(palavra_secreta)

    enforcou = acertou = False

    while (not acertou and not enforcou):
        chute = chute_usuario()


        if chute.upper() not in palavra_secreta:
            erros-=  1
            desenha_forca(erros)
            print(f'Errou! Tentativas restantes {erros}.')
            if erros == 0:
                enforcou = True

        marcar_acerto(palavra_secreta,chute,lista)


        if lista.count('_') == 0 :
            print('Acertou a palavra secreta!')
            acertou = True
            break
        for letra in lista:
            print(letra + ' ',end='')

    if acertou == True :
        print(f'A palavra secreta é: {palavra_secreta}',end="")


    elif enforcou == True:
        print('\nPerdeu! Enforcado!!')
        print(f'A palavra secreta é: {palavra_secreta}', end="")
def mensagem_bem_vindo():
    print('=-' * 50)
    print('BEM VINDOS AO JOGO DA FORCA!')
    print('=-' * 50)
def palavra_chave():
    palavras = []
    tema = str(input('Escolha do tema da forca. (P) para países, (F) para frutas e (A) para animais: ')).upper().strip()
    if tema == 'F':
        with open("frutas.txt", "r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                palavras.append(linha)

    elif tema == 'A':
        with open("animais.txt", "r",encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                palavras.append(linha)

    elif tema == 'P':
        with open("paises.txt", "r",encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                palavras.append(linha)

    else:
        print('Erro! Escolha invalida!')
        tema = str(input('Escolha do tema da forca. (P) para países, (F) para frutas e (A) para animais: ')).upper().sprit()
    n_aleatório = randint(0, len(palavras))
    palavra_secreta = palavras[n_aleatório].upper()
    return palavra_secreta
def dificuldade(palavra):
    dificuldade = str(input('Escolha a dificuldade, (f) para Fácil ou (d) para difícil: ')).upper().strip()
    while True:
        if dificuldade == 'F':
            erros = 7
            print()
            print(f'Você terá {erros} tentativas.')
            return erros
        elif dificuldade == 'D':
            erros = 7
            print()
            print(f'Você terá apenas {erros} tentativas.')
            return erros
        else:
            print('Escolha inválida.')
            dificuldade = input('Escolha a dificuldade, (f) para Fácil ou (d) para difícil: ').upper().strip()
def inicio_forca(palavra):
    return ["_" for letra in palavra]
def chute_usuario():
    chute = str(input('\nDigite um letra: ')).strip()
    return chute
def marcar_acerto(palavra_secreta,chute,lista):
    index = 0

    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            lista[index] = letra
        index += 1
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()