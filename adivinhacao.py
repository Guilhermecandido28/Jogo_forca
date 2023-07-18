string = '* Bem vindo ao jogo de adivinhação *'
print('* Bem vindo ao jogo de adivinhação *')
print('*'*len(string))
print()

numero_secreto = 42

chute = int(input('Digite o seu numero: '))

while True:
    if chute == numero_secreto:
        print('Você acertou')
        break
    elif chute == 999:
        print('Até mais!')
        break
    elif chute > numero_secreto:
        print('Errou! o numero secreto é menor.')
        chute = int(input('Tente Novamente, digite 999 para cancelar: '))
    elif chute < numero_secreto:
        print('Errou! o numero secreto é maior.')
        chute = int(input('Tente Novamente, digite 999 para cancelar: '))

