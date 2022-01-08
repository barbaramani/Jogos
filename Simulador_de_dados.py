#SIMULADOR DE DADOS
print('\033[32mSIMULADOR DE DADOS\033[m')

from random import randint

while True:
    jogar = input('Deseja jogar o dado? [S/N]:').upper()[0]
    dado = randint(1,6)
    if jogar != 'N' and jogar!='S':
         print('\033[35mTente novamente.\033[m')
    elif jogar == 'S':
        print(dado)
    elif jogar =='N':
        print('\033[7mObrigada e volte sempre!\033[m')
        break
