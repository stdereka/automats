import time


class Wolfram:
    def __init__(self):
        print('Выберите номер:', end=' ')
        self.number = int(input())
        self.band = None
        self.rules = [['111', None], ['110', None], ['101', None], ['100', None], ['011', None], ['010', None], ['001', None], ['000', None]]

    def read_band(self):
        print('Выберите ленту:', end=' ')
        path = input()
        file = open(path)
        band = file.read()
        self.band = list(band)
        print(self.band)

    def create_rules(self):
        N = list(str(bin(self.number))[2:])
        N = [0]*(8 - len(N)) + N
        i = 0
        for key in self.rules:
            key[1] = str(N[i])
            i += 1
        self.rules = dict(self.rules)
        print(self.rules)

    def run(self):
        while True:
            print(*self.band)
            newband = ['0']*len(self.band)
            for i in range(1, len(self.band) - 1):
                newband[i] = self.rules[self.band[i-1]+self.band[i]+self.band[i+1]]
            newband[0] = self.rules[self.band[-1]+self.band[0]+self.band[1]]
            newband[-1] = self.rules[self.band[-2]+self.band[-1]+self.band[0]]
            self.band[:] = newband[:]
            time.sleep(0.2)


W = Wolfram()
W.create_rules()
W.read_band()
W.run()
