class Field(object):
    def __init__(self, size):
        self.size = size

    def FieldOutput(self, field, score):
        for k in range(self.size):
            for l in range(self.size):
                print(field[k][l], end="")
            print()
        print('Счет:   ' + str(score))

    def FieldCreate(self):
            field = []
            for i in range(self.size):
                field.append([])
                for j in range(self.size):
                    field[i].append(' ')
                    if i == 0 or i == self.size - 1:
                        field[i][j] = '░'
                    elif j == 0 or j == self.size - 1:
                        field[i][j] = '░'
            return field