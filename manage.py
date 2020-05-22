import os
import time
from field import Field
from shake import Shake
import keyboard
from functions import *

score = 0
size = 40
speed = 10
F = Field(size)
field = F.FieldCreate()
shake = Shake(size, field, score, F)
field = shake.spawn()
field = PointRandom(field, size)
move = 'downward'
field_end = field
Game = True

rec = open('rec.txt', 'r')
recd = int(rec.read())
rec.close()
a = recd

while Game:
    field_end = field
    now = time.time()

    while time.time() - now < 1/speed:

        if keyboard.is_pressed('w'):
            move = 'upward'

        if keyboard.is_pressed('a'):
            move = 'left'

        if keyboard.is_pressed('s'):
            move = 'downward'

        if keyboard.is_pressed('d'):
            move = 'right'

        if keyboard.is_pressed('esc'):
            os.system('cls')
            Game = False

    if move == 'upward':
        field, Game = shake.move_upward()
    elif move == 'left':
        field, Game = shake.move_left()
    elif move == 'downward':
        field, Game = shake.move_downward()
    elif move == 'right':
        field, Game = shake.move_right()

    score = shake.print_score()
    
    if recd <= int(score):
        recd = int(score)

    #Выводим что получилось
    os.system('cls')
    F.FieldOutput(field, score, recd)

if a < recd:
    rec = open('rec.txt', 'w')
    rec.write(str(recd))
    rec.close()

os.system('cls')
F.FieldOutput(field_end, score, recd)
print("Game Over")
