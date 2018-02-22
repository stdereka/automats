class Machine:
    def __init__(self):
        self.conditions = {}
        self.band = []
        self.condition = 'start'

    def read_band(self):
        print('Выберите ленту:', end=' ')
        path = input()
        file = open(path)
        band = file.read()
        self.band = list(band)

    def read_condition_table(self):
        print('Выберите программу:', end=' ')
        path = input()
        file = open(path)
        conditions = file.readlines()
        for line in conditions:
            words = line.split('|')
            if words[0] not in self.conditions:
                self.conditions[words[0]] = {}
            self.conditions[words[0]][words[1]] = tuple(words[2:])
        print(self.conditions)

    def work(self):
        print('Введите начальную позицию:', end=' ')
        current = int(input())
        print()
        maxnum = len(self.band)
        while self.condition != 'finish':
            if self.band[current] in self.conditions[self.condition]:
                direct = self.conditions[self.condition][self.band[current]][2][:1]
                currcond = self.condition
                print('Текущее состояние:', currcond)
                print('Символ на ленте:', self.band[current] + ', позиция:', current)
                print('Меняю', self.band[current], 'на', self.conditions[currcond][self.band[current]][0])
                print('Перехожу в состояние', self.conditions[currcond][self.band[current]][1])
                self.condition = self.conditions[currcond][self.band[current]][1]
                self.band[current] = self.conditions[currcond][self.band[current]][0]
                if direct == 'l' and current != 0:
                    print('Смещаюсь влево')
                    print()
                    current -= 1
                elif direct == 'r' and current != maxnum-1:
                    print('Смещаюсь вправо')
                    print()
                    current += 1
                else:
                    print('Завершаю работу')
                    print()
                    self.condition = 'finish'
        print('Выходная лента:', "".join(self.band))

T = Machine()
T.read_band()
T.read_condition_table()
T.work()
