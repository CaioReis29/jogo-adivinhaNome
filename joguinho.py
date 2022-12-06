secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances == 0:
        print('Você perdeu:(')
        break
    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print('Po, isso não vale kkk só pode digitar uma letra. enfim... ')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Boa mlk, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Vish... a letra "{letra}" não existe na palavra secreta.')

        digitadas.pop()

    print(digitadas)

    secretoTemporario = ''
    for letraSecreta in secreto:
        if letraSecreta in digitadas:
            secretoTemporario += letraSecreta
        else:
            secretoTemporario += '*'
    if secretoTemporario == secreto:
        print(f'AEEEEEEEE, você ganhou!!! A palavra secreta é: {secretoTemporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secretoTemporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()