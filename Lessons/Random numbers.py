import random as rnd


class Random_range():
    """Создание класса для работы со случайными значениями
    Этот класс сделан для тренировки, лучше использовать Pandas-frame для таких расчетов
    """
    def __init__(self, size=[2, 50], name=None):
        """Создание массива рандомных значений

        Args:
            size (list, optional): [description]. Defaults to [2, 50].
            name ([type], optional): [description]. Defaults to None.
        """
        self.value = [[(rnd.random() * 100) // 1 for x in range(size[1])]
                      for y in range(size[0])]
        for i in range(len(self.value)):
            self.value[i].insert(0, 'Row %s' % i)
        self.name = name

    def print(self):

        print("%s's values" % self.name)
        for i in range(len(self.value)):
            print(self.value[i])

    def plus(self, number_one, number_two):
        answer = [
            self.value[number_one][i] + self.value[number_two][i]
            for i in range(len(self.value[0]))
        ]
        self.value.append(answer)
        self.value[len(self.value)-1][0]= 'Plus %s + %s'% (number_one, number_two)

    def minus(self, number_one, number_two):
        answer = [
            self.value[number_one][i] - self.value[number_two][i]
            for i in range(len(self.value[0]))
        ]
        self.value.append(answer)

a = Random_range(name='First',size=[3,10])
a.plus(1,2)
a.print()