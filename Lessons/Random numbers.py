import random as rnd


class Random_range():
    """Создание класса для работы со случайными значениями
    Этот класс сделан для тренировки, лучше использовать Pandas-frame для таких расчетов или хотя бы numpy. 
    Но для тренировки так
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
            self.value[i].insert(0, 'R%s' % i)
        self.name = name

    def print(self):

        print("%s's values" % self.name)
        for i in range(self.sizeY):
            print(self.value[i])

    def plus(self, row_one, row_two):
        answer = [
            self.value[row_one][i] + self.value[row_two][i]
            for i in range(self.sizeX)
        ]
        self.value.append(answer)
        self.value[self.sizeY][0] = '%s + %s' % (self.value[row_one][0], self.value[row_two][0])
        self.sizeY += 1

    def minus(self, row_one, row_two):
        answer = [
            self.value[row_one][i] - self.value[row_two][i]
            for i in range(self.sizeX)
        ]
        self.value.append(answer)
        self.value[self.sizeY][0] = '%s-%s' % (self.value[row_one][0], self.value[row_two][0])
        
        self.sizeY += 1

    def sigma(self, row,deg=2):
        suma = 0
        for i in range(1, self.sizeX):
            suma += self.value[row][i]
        mid = suma / self.sizeX
        sigma = []

        for i in range(1, self.sizeX):
            sigma.append((mid - self.value[row][i])**deg / self.sizeX)

        self.value.append(sigma)
        self.value[self.sizeY][0] = 'Si%s: %s' % (deg,self.value[row][0])
        self.sizeY += 1

        # for i in range(1, self.sizeX):
        #     suma += self.value[row][i]
        #     self.value.append(suma)


a = Random_range(name='First', sizeY=2)
a.plus(0, 1)
a.sigma(0,2)
a.sigma(1,2)
a.sigma(2,2)
a.sigma(0,4)
a.sigma(1,4)
a.sigma(2,4)
a.print()