import random as rnd
"""
    Создает n раз массивы (представлены ниже) из случайных чисел, нужной длины и находит сигму (ниже Si-deg) в 2 и в 
    других cтепенях (ниже deg), в том числе и в модуля, сравнивает находится ли значения 
    Si(a) + Si(b) между Si(a+b) и Si(a-b), если да то помечает.

"""


class Random_range():
    """Создание класса для работы со случайными значениями
    Этот класс сделан для тренировки, лучше использовать Pandas-frame для таких расчетов или хотя бы numpy. 
    Но для тренировки так
    """
    def __init__(self, sizeY=2, sizeX=10, name=None, qual=100):
        """Создание массива рандомных значений

        Args:
            sizeY (int, optional): [description]. Defaults to 2.
            sizeX (int, optional): [description]. Defaults to 10.
            name ([type], optional): [description]. Defaults to None.
            qual (int, optional): [description]. Defaults to 100.
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
            for x in range(self.sizeX + 1):
                if type(self.value[y][x]) == str:
                    output += ' |{0: <14}|'.format(self.value[y][x])

                else:
                    output += ' {0: >10.2f}'.format(self.value[y][x])

            print(output)

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

    def findsigma(self, row, deg=2):
        """Возвращает дисперсию степени deg. 1 - для модуля

        Args:
            row (int) Номер строки
            deg (int, optional): [description]. Defaults to 2.
        """
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

    def summa(self, row):
        suma = 0
        for i in range(self.sizeX):
            suma += self.value[row][i]
        return suma


print(' 2 - 4 - || ')
for n in range(200):
    a = Random_range(name=str(n), sizeX=50)
    # Создание массива с нужными значениями. Эту часть можно улучшить и сделать красивой, но не успел еще.
    a.plus(0, 1)
    a.minus(0, 1)

    a.findsigma(0)
    a.findsigma(1)

    a.findsigma(2)
    a.findsigma(3)

    a.findsigma(0, 4)
    a.findsigma(1, 4)

    a.findsigma(2, 4)
    a.findsigma(3, 4)

    a.findsigma(0, 1)
    a.findsigma(1, 1)

    a.findsigma(2, 1)
    a.findsigma(3, 1)

    # для проверки:
    # a.print()
    quality_indicator = [0, 0, 0, 0]
    for s in range(1, 4):
        r0 = a.summa(s * 4)
        r1 = a.summa(s * 4 + 1)
        rplus = a.summa(s * 4 + 2)
        rminus = a.summa(s * 4 + 3)
        # проверка
        # print('%s %s %s %s'%(r0,r1,rplus,rminus))

        if rplus < r0 + r1 < rminus or rminus < r0 + r1 < rplus:
            quality_indicator[s] = '+'
        else:
            quality_indicator[s] = ' '

    print(' {0} | {1} | {2} '.format(quality_indicator[1],
                                     quality_indicator[2],
                                     quality_indicator[3]))
