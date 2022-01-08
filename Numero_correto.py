print('\033[36m NÚMERO CORRETO\033[m')

import random

numero = random.randint(1,20)

escolha = int(input('Adivinhe o número que estou pensando (1 a 20):'))

while True:

    if numero == escolha:
        print(f'\033[36mParabéns, você acertou. Pensei no número {numero}.\033[m')
        jogar = input('Deseja jogar novamente: [S/N]:').upper()[0]
        if jogar == 'S':
            numero = random.randint(1,20)
            escolha = int(input('Adivinhe o número que estou pensando (1 a 20):'))
        else:
            print('\033[34mObrigada e volte sempre!\033[m')
            break
    elif numero!=escolha:
        if numero>escolha:
            escolha = int(input('Pensei em um número \033[32mmais alto\033[m. Tente novamente:'))
        elif numero < escolha:
            escolha = int(input('Pensei em um número \033[35mmais baixo\033[m. Tente novamente:'))
