import random as rnd


class Random_range():
    """Создание класса для работы со случайными значениями
    Этот класс сделан для тренировки, лучше использовать Pandas-frame для таких расчетов
    """
    def __init__(self, sizeY=2, sizeX=10, name=None):
        """Создание массива рандомных значений

        Args:
            size (list, optional): [description]. Defaults to [2, 50].
            name ([type], optional): [description]. Defaults to None.
        """
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.value = [[(rnd.random() * 100) // 1 for x in range(sizeX)]
                      for y in range(sizeY)]
        for i in range(self.sizeY):
            self.value[i].insert(0, 'Row %s' % i)
        self.name = name

    def print(self):

        print("%s's values" % self.name)
        for i in range(self.sizeY):
            print(self.value[i])

    def plus(self, number_one, number_two):
        answer = [
            self.value[number_one][i] + self.value[number_two][i]
            for i in range(self.sizeX)
        ]
        self.value.append(answer)
        self.value[self.sizeY][0] = 'Plus %s + %s' % (number_one, number_two)
        self.sizeY += 1

    def minus(self, number_one, number_two):
        answer = [
            self.value[number_one][i] - self.value[number_two][i]
            for i in range(self.sizeX)
        ]
        self.value.append(answer)
        self.value[self.sizeY][0] = 'Minus %s - %s' % (number_one, number_two)
        self.sizeY += 1

    def sigma(self, row):

        for i in range(1, self.sizeX):
            suma += self.value[row][i]
        mid = suma / self.sizeX

        for i in range(1, self.sizeX):
            sigma = (mid - self.value[row][i])**2 / self.sizeX

        self.value.append(sigma)
        self.value[self.sizeY - 1][0] = 'Sigma %s' % (row)

        for i in range(1, self.sizeX):
            suma += self.value[row][i]
            self.value.append[(suma)


a = Random_range(name='First', sizeY=3)
a.plus(1, 2)
a.print()