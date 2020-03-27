import random

def PointRandom(field, size):
    while True:
        y = random.randint(1, size - 2)
        x = random.randint(1, size - 2)
        list_of_walls = ['', '0']
        if field[y][x] in list_of_walls:
            pass
        else:
            break
    field[y][x] = "@"
    return field

def Impact(field, y, x):
    list_of_walls = ['░', '0']
    if field[y][x] in list_of_walls:
        return True
    elif field[y][x] == '@':
        return 'spawn'
    else:
        return False

def move(field, coordinate_y, coordinate_x, pref_y, pref_x):
    field[pref_y][pref_x] = ''
    coordinate_y = pref_y
    coordinate_x = pref_x
    return field, coordinate_y, coordinate_x

def spawn_body(list_y, list_x):
    list_y.append(list_y[-1])
    list_x.append(list_x[-1])
    return list_y, list_x

def hvost(list_y, list_x, y, x, field):
    for o in range(len(list_y)):
        y1 = list_y[o-1]
        x1 = list_x[o-1]
        field[list_y[o-1]][list_x[o-1]] = ' '
        list_y[o-1] = y
        list_x[o-1] = x
        field[list_y[o-1]][list_x[o-1]] = '0'
        y = y1
        x = x1
    return list_y, list_x, field

