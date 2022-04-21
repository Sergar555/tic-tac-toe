def first_player():
    i = int(input('ПЕРВЫЙ ИГРОК, укажите номер строки для поля, в которое хоитите поставить крестик.\n'))
    j = int(input('А теперь номер столбца\n'))
    if (i or j) not in range(1,4):
       print('Значения должны быть в диапазоне 1-3!')
       return first_player()
    elif playing_field[i][j] != '-':
        print('В поле уже есть значек! Выберите другое!')
        return first_player()
    else:
        playing_field[i][j] = 'X'

def second_player():
    i = int(input('ВТРОЙ ИГРОК, укажите номер строки для поля, в которое хоитите поставить нолик.\n'))
    j = int(input('А теперь номер столбца\n'))
    if (i or j) not in range(1,4):
       print('Значения должны быть в диапазоне 1-3!')
       return second_player()
    elif playing_field[i][j] != '-':
        print('В поле уже есть значек! Выберите другое!')
        return second_player()
    else:
        playing_field[i][j] = '0'

def combination_check_X():
    if any([
        playing_field[1][1] == playing_field[1][2] == playing_field[1][3] == 'X',
        playing_field[2][1] == playing_field[2][2] == playing_field[2][3] == 'X',
        playing_field[3][1] == playing_field[3][2] == playing_field[3][3] == 'X',
        playing_field[1][1] == playing_field[2][1] == playing_field[3][1] == 'X',
        playing_field[1][2] == playing_field[2][2] == playing_field[3][2] == 'X',
        playing_field[1][3] == playing_field[2][3] == playing_field[3][3] == 'X',
        playing_field[1][1] == playing_field[2][2] == playing_field[3][3] == 'X',
        playing_field[3][1] == playing_field[2][2] == playing_field[1][3] == 'X'
    ]):
        winner = 'Первый игрок победил!'
        print(winner)
    else:
        winner = None
    return winner

def combination_check_0():
    if any([
        playing_field[1][1] == playing_field[1][2] == playing_field[1][3] == '0',
        playing_field[2][1] == playing_field[2][2] == playing_field[2][3] == '0',
        playing_field[3][1] == playing_field[3][2] == playing_field[3][3] == '0',
        playing_field[1][1] == playing_field[2][1] == playing_field[3][1] == '0',
        playing_field[1][2] == playing_field[2][2] == playing_field[3][2] == '0',
        playing_field[1][3] == playing_field[2][3] == playing_field[3][3] == '0',
        playing_field[1][1] == playing_field[2][2] == playing_field[3][3] == '0',
        playing_field[3][1] == playing_field[2][2] == playing_field[1][3] == '0'
    ]):
        winner = 'Второй игрок победил!'
        print(winner)
    else:
        winner = None
    return winner

def game(n):
    first_player()
    for i in range(len(playing_field)):
        print(' '.join(playing_field[i]))
    winner = combination_check_X()
    if winner:
        return
    second_player()
    for i in range(len(playing_field)):
        print(' '.join(playing_field[i]))
    winner = combination_check_0()
    if winner:
        return
    if n > 5:
        stop = input('Если хотите закончить игру, введите любой символ, если хотите продолжить - нажмите "Пробел", затем "Ввод"')
        if stop == ' ':
            return game(n+2)
        else:
            return 'Игра завершена!'
    return game(n+2)

print('Играем в крестики-нолики!')
print('Чтобы сделать ход, введите номер строки и номер столбца,')
print('для поля, в которое вы хотите поставить крестит или нолик.')
print('Первый игрок играет крестиками второй ноликами!!!\n')

playing_field = [
    (' ', '1', '2', '3'),
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-'],
    ['3', '-', '-', '-'],
]
n = 2

for i in range(len(playing_field)):
    print(' '.join(playing_field[i]))

game(n)

