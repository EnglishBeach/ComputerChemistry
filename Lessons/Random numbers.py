import random as rnd


class Random_range():
    """Создание класса для работы со случайными значениями
    Этот класс сделан для тренировки, лучше использовать Pandas-frame для таких расчетов или хотя бы numpy. 
    Но для тренировки так
    """
    def __init__(self, sizeY=2, sizeX=10, name=None, qual=100):
        """Создание массива рандомных значений

        Args:
            size (list, optional): [description]. Defaults to [2, 50].
            name ([type], optional): [description]. Defaults to None.
        """
        self.qual = qual
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.value = [[((rnd.random() * 100) - 50) // 1 for x in range(sizeX)]
                      for y in range(sizeY)]
        for i in range(self.sizeY):
            self.value[i].append('R%s' % i)
        self.name = name

    def print(self):

        print("%s's values: " % self.name)
        
        for y in range(self.sizeY):
            output = ''
            for x in range(self.sizeX+1):
                if type(self.value[y][x]) == str:
                    output += ' |{0}'.format(self.value[y][x])
                    
                else:
                    output += ' {0: >10.2e}'.format(self.value[y][x])
                    
            
            print(output)
    # print(self.value[i])

    def plus(self, row_one, row_two):
        answer = [(self.value[row_one][i] + self.value[row_two][i]) //
                  (1 / self.qual) / self.qual for i in range(self.sizeX)]
        self.value.append(answer)
        name = '%s + %s' % (self.value[row_one][self.sizeX],
                            self.value[row_two][self.sizeX])
        self.value[self.sizeY].append(name)
        self.sizeY += 1

    def minus(self, row_one, row_two):
        answer = [(self.value[row_one][i] - self.value[row_two][i]) //
                  (1 / self.qual) / self.qual for i in range(self.sizeX)]
        self.value.append(answer)
        name = '%s - %s' % (self.value[row_one][self.sizeX],
                            self.value[row_two][self.sizeX])
        self.value[self.sizeY].append(name)
        self.sizeY += 1

    def sigma(self, row, deg=2):
        suma = 0
        for i in range(self.sizeX):
            suma += self.value[row][i]
        mid = suma / self.sizeX
        sigma = []

        for i in range(self.sizeX):
            if deg == 1:
                sigma.append((abs(mid - self.value[row][i]) / self.sizeX) //
                             (1 / self.qual) / self.qual)
            else:
                sigma.append(((mid - self.value[row][i])**deg / self.sizeX) //
                             (1 / self.qual) / self.qual)

        self.value.append(sigma)
        name = 'Si%s: %s' % (deg, self.value[row][self.sizeX])
        self.value[self.sizeY].append(name)
        self.sizeY += 1

        # for i in range(1, self.sizeX):
        #     suma += self.value[row][i]
        #     self.value.append(suma)


a = Random_range(name='First', sizeY=2,sizeX=10)
a.plus(0, 1)
a.sigma(0, 2)
a.sigma(1, 2)
a.sigma(2, 2)
a.sigma(0, 4)
a.sigma(1, 4)
a.sigma(2, 4)
a.print()