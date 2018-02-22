import time


class Life:
    def __init__(self):
        file = open('field.txt')
        f = file.readlines()
        for i in range(len(f)):
            f[i] = list(f[i][:-1])
        self.field = f[:]

    def print(self):
        for i in range(len(self.field)):
            print(*self.field[i])

    def new(self, x, y):
        count = 0
        if self.field[x][y] == '*':
            if self.field[x][y-1] == '*':
                count += 1
            if self.field[x][y+1] == '*':
                count += 1
            if self.field[x-1][y] == '*':
                count += 1
            if self.field[x+1][y] == '*':
                count += 1
            if self.field[x+1][y+1] == '*':
                count += 1
            if self.field[x+1][y-1] == '*':
                count += 1
            if self.field[x-1][y+1] == '*':
                count += 1
            if self.field[x-1][y-1] == '*':
                count += 1
            if count in (2, 3):
                return '*'
            else:
                return '.'
        elif self.field[x][y] == '.':
            if self.field[x][y-1] == '*':
                count += 1
            if self.field[x][y+1] == '*':
                count += 1
            if self.field[x-1][y] == '*':
                count += 1
            if self.field[x+1][y] == '*':
                count += 1
            if self.field[x+1][y+1] == '*':
                count += 1
            if self.field[x+1][y-1] == '*':
                count += 1
            if self.field[x-1][y+1] == '*':
                count += 1
            if self.field[x-1][y-1] == '*':
                count += 1
            if count == 3:
                return '*'
            else:
                return '.'

    def work(self):
        while True:
            self.print()
            field = self.field[:]
            nf = [['0']*len(field[0]) for k in range(len(field))]
            for i in range(1, len(field)-1):
                for j in range(1, len(field[0])-1):
                    nf[i][j] = self.new(i, j)
            self.field = nf[:]
            print()
            time.sleep(0.5)

G = Life()
G.work()
