import numpy as np
import matplotlib.pyplot as plt

TIMELIMIT = 100

class Agent:
    """エージェントを表現するクラス定義"""
    def __init__(self, cat):
        self.category = cat
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 1
    def calcnext(self):
        if self.category == 0:
            self.cat0()
        else:
            print('ERROR\n')
    def cat0(self):#エージェントの具体的な行動
        self.dx = self.reverse(self.dx)
        self.dy = self.reverse(self.dy)

        self.x += self.dx
        self.y += self.dy
    def reverse(self, i):
        if i == 0:
            return 4
        else:
            return 0
    def putstate(self):
        print(self.x, self.y)

def calcn(a):
    """次時刻の状態を計算"""
    for i in range(len(a)):
        a[i].calcnext()#シングルだと一回だけ
        a[i].putstate()

        xlist.append(a[i].x)
        ylist.append(a[i].y)

a = [Agent(0)]

xlist = []
ylist = []

for t in range(TIMELIMIT):
    calcn(a)

    plt.clf()
    plt.axis([0, 60, 0, 60])
    plt.plot(xlist, ylist, ".")
    plt.pause(0.01)
    xlist.clear()
    ylist.clear()
plt.show()
