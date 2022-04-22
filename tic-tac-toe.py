def player_turn(n):
    i = int(input(f'{players[0][n].upper()}, укажите номер строки для поля, в которое хоитите поставить крестик.\n'))
    j = int(input('А теперь номер столбца\n'))
    if (i or j) not in range(1,4):
       print('Значения должны быть в диапазоне 1-3!')
       return player_turn(n)
    elif playing_field[i][j] != '-':
        print('В поле уже есть значек! Выберите другое!')
        return player_turn(n)
    else:
        playing_field[i][j] = players[1][n]

def combination_check(n):
    if any([
        playing_field[1][1] == playing_field[1][2] == playing_field[1][3] == players[1][n],
        playing_field[2][1] == playing_field[2][2] == playing_field[2][3] == players[1][n],
        playing_field[3][1] == playing_field[3][2] == playing_field[3][3] == players[1][n],
        playing_field[1][1] == playing_field[2][1] == playing_field[3][1] == players[1][n],
        playing_field[1][2] == playing_field[2][2] == playing_field[3][2] == players[1][n],
        playing_field[1][3] == playing_field[2][3] == playing_field[3][3] == players[1][n],
        playing_field[1][1] == playing_field[2][2] == playing_field[3][3] == players[1][n],
        playing_field[3][1] == playing_field[2][2] == playing_field[1][3] == players[1][n]
    ]):
        winner = f'{players[0][n]} игрок победил!'
        print(winner)
    else:
        winner = None
    return winner

def game(m):
    for n in range(2):
        player_turn(n)
        for i in range(len(playing_field)):
            print(' '.join(playing_field[i]))
        winner = combination_check(n)
        if winner:
            return
    if m >= 3:
        stop = input('Если хотите закончить игру, введите любой символ, если хотите продолжить - нажмите "Пробел", затем "Ввод"')
        if stop == ' ':
            return game(m+1)
        else:
            return 'Игра завершена!'
    return game(m+1)

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

players = (('Первый игрок', 'Второй игрок'), ('X', '0'))

m = 1

for i in range(len(playing_field)):
    print(' '.join(playing_field[i]))

game(m)

