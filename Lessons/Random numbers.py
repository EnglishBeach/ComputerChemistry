import random as rnd


class Random_range():
    def __init__(self, size=[2, 50], name=None):
        self.value = [[(rnd.random() * 100) // 1 for x in range(size[1])]
                      for y in range(size[0])]
        self.name = name

    def print(self):
        print("%s's values" % self.name)
        for i in range(len(self.value)):
            print(self.value[i])
