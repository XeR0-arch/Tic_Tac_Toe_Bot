arr = ['*','*','*','*','*','*','*','*','*']
check = ['*']
wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def print_grid():
    for i in range(9):
        if i == 2 or i == 5:
            print(arr[i])
        else:
            print(arr[i], end = " ")
    print()

def check_wins():
    for win in wins:
        if (arr[win[0]]=='O' and arr[win[1]]=='O' and arr[win[2]]=='*'):
            arr[win[2]] = 'O'
            return True
        elif (arr[win[0]]=='O' and arr[win[1]]=='*' and arr[win[2]]=='O'):
            arr[win[1]] = 'O'
            return True
        elif (arr[win[0]]=='*' and arr[win[1]]=='O' and arr[win[2]]=='O'):
            arr[win[0]] = 'O'
            return True
    return False

def block_win():
    for win in wins:
        if (arr[win[0]]=='X' and arr[win[1]]=='X' and arr[win[2]]=='*'):
            arr[win[2]] = 'O'
            return True
        elif (arr[win[0]]=='X' and arr[win[1]]=='*' and arr[win[2]]=='X'):
            arr[win[1]] = 'O'
            return True
        elif (arr[win[0]]=='*' and arr[win[1]]=='X' and arr[win[2]]=='X'):
            arr[win[0]] = 'O'
            return True
    return False

def set_win():
    for win in wins:
        if (arr[win[0]]=='O' and arr[win[1]]=='*' and arr[win[2]]=='*'):
            arr[win[2]] = 'O'
            return True
        elif (arr[win[0]]=='*' and arr[win[1]]=='O' and arr[win[2]]=='*'):
            arr[win[2]] = 'O'
            return True
        elif (arr[win[0]]=='*' and arr[win[1]]=='*' and arr[win[2]]=='O'):
            arr[win[0]] = 'O'
            return True
    return False

def first_move():
    if arr[4] == '*':
        arr[4] = 'O'
        return True
    elif arr[4] == 'X' and arr[6] == '*':
        arr[6] = 'O'
        return True
    return False

def check_winner():
    for win in wins:
        if (arr[win[0]]=='O' and arr[win[1]]=='O' and arr[win[2]]=='O'):
            print("O wins!!!")
            return True
        elif (arr[win[0]]=='X' and arr[win[1]]=='X' and arr[win[2]]=='X'):
            print("X wins!!!")
            return True
    return False

while list(set(arr) & set(check)) != []:
    print_grid()
    if check_winner():
        break
    a = int(input("Enter a box: "))
    if arr[a] == '*':
        arr[a] = 'X'
    else:
        print("See the grid again and enter a valid aquare")
        continue
    if first_move():
        continue
    if check_wins():
        continue
    elif block_win():
        continue
    else:
        set_win()
        continue
