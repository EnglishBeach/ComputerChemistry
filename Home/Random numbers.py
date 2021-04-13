import random as rnd
"""
    Создает массив из случайных значений А и В
        A0 A1 A2 A3...
        B0 B1 B2 B3...
    Создает строку суммы и разности 2 выбранных строк
    Считает функцию 'невязки' вида:
            Si = (X-x)^deg/N, где X - среднее значение по строке, N - количество значений, n - степень 
    Проверяет:  Si(A+B) < Si(A)+Si(B) < Si(A-B) или
                Si(A-B) < Si(A)+Si(B) < Si(A+B)
        Если да = то правило сложения выполняется => +
        Если нет = то не выполняется => ' ' 

"""


class Random_range():
    """
    Создание массива случайных значений, с возможностью складывать/вычитать строки случайных сначений 1 из другой, находить функцию невязки для разных степеней.

    Этот класс сделан для тренировки, лучше использовать Pandas-frame для таких расчетов или хотя бы numpy. 
    """
    def __init__(self,
                 sizeY=2,
                 sizeX=10,
                 accuracy=100,
                 normal=False,
                 name=None):
        """
        Создает массив из случайных значений А и В
        A0 A1 A2 A3...
        B0 B1 B2 B3...

        Args:
            sizeY (int, optional): Количество строк массива с рандомными значениями. Defaults to 2.
            sizeX (int, optional): Длина строки, фактически размер выборки 1-ой переменной. Defaults to 10.
            accuracy (int, optional): Количество знаков после . случайного числа. Ограничивает огромные хвосты в расчетах или выводе. Defaults to 100.
            normal (byl, optional): Условие нормировки значений (деление на размах выборки). Defaults to False.
        """
        self.name = name
        self.normal = normal
        self.accuracy = accuracy
        self.sizeX = sizeX
        self.sizeY = sizeY
        if normal == True: nkoef = 1
        else: nkoef = 100
        self.value = [[((rnd.random() * nkoef) - nkoef // 2) // 1
                       for x in range(sizeX)] for y in range(sizeY)]
        for i in range(self.sizeY):
            self.value[i].append('R%s' % i)

    def print(self):
        """
        Выводит на экран значения всего массива
        """

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
        """
        Создает строку суммы 2 выбранных строк

        Args:
            row_one ([type]): 1 строка
            row_two ([type]): 2 строка
        """
        answer = [(self.value[row_one][i] + self.value[row_two][i]) //
                  (1 / self.accuracy) / self.accuracy
                  for i in range(self.sizeX)]
        self.value.append(answer)
        name = '%s + %s' % (self.value[row_one][self.sizeX],
                            self.value[row_two][self.sizeX])
        self.value[self.sizeY].append(name)
        self.sizeY += 1

    def minus(self, row_one, row_two):
        """
        Создает строку разности 2 выбранных строк 1строка - 2строка

        Args:
            row_one ([type]): 1 строка
            row_two ([type]): 2 строка
        """
        answer = [(self.value[row_one][i] - self.value[row_two][i]) //
                  (1 / self.accuracy) / self.accuracy
                  for i in range(self.sizeX)]
        self.value.append(answer)
        name = '%s - %s' % (self.value[row_one][self.sizeX],
                            self.value[row_two][self.sizeX])
        self.value[self.sizeY].append(name)
        self.sizeY += 1

    def findsigma(self, row, deg=2):
        """
        Считает функцию 'невязки' вида:
            Si = (X-x)^deg/N, где X - среднее значение по строке, N - количество значений, n - степень 
            (n=2 - обычная дисперсия), n=1 - модуль числа

        Args:
            row (int) Номер строки
            deg (int, optional): Степень в функции 'невязки'. Неустойчива к четным дробным (вызовет ошибку). 
                = 2 - обычная дисперсия. 
                = 1 - модуль
                Defaults to 2.
        """
        suma = 0
        for i in range(self.sizeX):
            suma += self.value[row][i]
        mid = suma / self.sizeX
        sigma = []

        for i in range(self.sizeX):
            if deg == 1:
                sigma.append((abs(mid - self.value[row][i]) / self.sizeX) //
                             (1 / self.accuracy) / self.accuracy)
            else:
                sigma.append(((mid - self.value[row][i])**deg / self.sizeX) //
                             (1 / self.accuracy) / self.accuracy)

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
#Можно сделать лучше вывод, но это трудоемко и не столь важно
for n in range(200):
    # Создание массива с нужными значениями. Эту часть можно улучшить и сделать красивой, но не успел еще.
    a = Random_range(name=str(n), sizeX=10)
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

    # Индикатор сходимости для каждой степени
    quality_indicator = [0, 0, 0, 0]

    # Пробелается по каждому блоку из вычесленных Si для каждой степени
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
