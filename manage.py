import os
import time
from field import Field
from shake import Shake
import keyboard
from functions import *

score = 0
size = 50
F = Field(size)
field = F.FieldCreate()
shake = Shake(size, field, score, F)
field = shake.spawn()
field = PointRandom(field, size)
move = 'downward'
field_end = field
while True:
    try:
        field_end = field

        if move == 'upward':
            field = shake.move_upward()
        elif move == 'left':
            field = shake.move_left()
        elif move == 'downward':
            field = shake.move_downward()
        elif move == 'right':
            field = shake.move_right()
        
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
            break

        score = shake.print_score()
        
        #Выводим что получилось
        F.FieldOutput(field, score)
        time.sleep(0.1)
        os.system('cls')
    except:
        break
F.FieldOutput(field_end, score)
print("Game Over")
