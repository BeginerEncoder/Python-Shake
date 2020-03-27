from functions import *

class Shake(object):
    def __init__(self, size, field, score, F):
        self.size = size
        self.field = field
        self.score = score
        self.coordinate_y = self.size // 2
        self.coordinate_x = self.size // 2
        self.list_y = []
        self.list_x = []
        self.pref_y = 0
        self.pref_x = 0
        self.F = F

    def spawn(self):
        self.field[self.coordinate_y][self.coordinate_x] = ''
        self.list_y.append(self.coordinate_y - 1)
        self.list_x.append(self.coordinate_x)
        return self.field

    def move_upward(self):
        if Impact(self.field, self.coordinate_y-1, self.coordinate_x) == True:
            raise Break()
        elif Impact(self.field, self.coordinate_y-1, self.coordinate_x) == 'spawn':
            self.score += 1
            self.list_y, self.list_x, self.field = hvost(self.list_y, self.list_x, self.coordinate_y, self.coordinate_x, self.field)
            self.list_y, self.list_x = spawn_body(self.list_y, self.list_x)
            self.field, self.coordinate_y, self.coordinate_x = move(self.field,self.coordinate_y,self.coordinate_x,self.coordinate_y-1,self.coordinate_x)
            self.field = PointRandom(self.field, self.size)
        else:
            self.list_y, self.list_x, self.field = hvost(self.list_y, self.list_x, self.coordinate_y, self.coordinate_x, self.field)
            self.field, self.coordinate_y, self.coordinate_x = move(self.field,self.coordinate_y,self.coordinate_x,self.coordinate_y-1,self.coordinate_x)
        return self.field
    
    def move_left(self):
        if Impact(self.field, self.coordinate_y, self.coordinate_x-1) == True:
            raise Break()
        elif Impact(self.field, self.coordinate_y, self.coordinate_x-1) == 'spawn':
            self.score += 1
            self.list_y, self.list_x, self.field = hvost(self.list_y, self.list_x, self.coordinate_y, self.coordinate_x, self.field)
            self.list_y, self.list_x = spawn_body(self.list_y, self.list_x)
            self.field, self.coordinate_y, self.coordinate_x = move(self.field,self.coordinate_y,self.coordinate_x,self.coordinate_y,self.coordinate_x-1)
            self.field = PointRandom(self.field, self.size)
        else:
            self.list_y, self.list_x, self.field = hvost(self.list_y, self.list_x, self.coordinate_y, self.coordinate_x, self.field)
            self.field, self.coordinate_y, self.coordinate_x = move(self.field,self.coordinate_y,self.coordinate_x,self.coordinate_y,self.coordinate_x-1)
        return self.field

    def move_downward(self):
        if Impact(self.field, self.coordinate_y+1, self.coordinate_x) == True:
            raise Break()
        elif Impact(self.field, self.coordinate_y+1, self.coordinate_x) == 'spawn':
            self.score += 1
            self.list_y, self.list_x, self.field = hvost(self.list_y, self.list_x, self.coordinate_y, self.coordinate_x, self.field)
            self.list_y, self.list_x = spawn_body(self.list_y, self.list_x)
            self.field, self.coordinate_y, self.coordinate_x = move(self.field,self.coordinate_y,self.coordinate_x,self.coordinate_y + 1,self.coordinate_x)
            self.field = PointRandom(self.field, self.size)
        else:
            self.list_y, self.list_x, self.field = hvost(self.list_y, self.list_x, self.coordinate_y, self.coordinate_x, self.field)
            self.field, self.coordinate_y, self.coordinate_x = move(self.field, self.coordinate_y, self.coordinate_x, self.coordinate_y + 1, self.coordinate_x)
        return self.field

    def move_right(self):
        if Impact(self.field, self.coordinate_y, self.coordinate_x+1) == True:
            raise Break()
        elif Impact(self.field, self.coordinate_y, self.coordinate_x+1) == 'spawn':
            self.score += 1
            self.list_y, self.list_x, self.field = hvost(self.list_y, self.list_x, self.coordinate_y, self.coordinate_x, self.field)
            self.list_y, self.list_x = spawn_body(self.list_y, self.list_x)
            self.field, self.coordinate_y, self.coordinate_x = move(self.field,self.coordinate_y,self.coordinate_x,self.coordinate_y,self.coordinate_x + 1)
            self.field = PointRandom(self.field, self.size)
        else:
            self.list_y, self.list_x, self.field = hvost(self.list_y, self.list_x, self.coordinate_y, self.coordinate_x, self.field)
            self.field, self.coordinate_y, self.coordinate_x = move(self.field, self.coordinate_y, self.coordinate_x, self.coordinate_y, self.coordinate_x + 1)
        return self.field

    def print_score(self):
        return self.score

    def print_list(self):
        print(self.list_y)
        print(self.list_x)