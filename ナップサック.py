import random

weights = [87,66,70,25,33,24,89,63,23,54]
values = [96,55,21,58,41,81,8,99,59,62]
N = len(weights)
SEED = 32767
R = 10#実験回数

def solvekp(p, weightlimit, nlimit, N):
    maxvalue = 0
    mweight = 0
    bestp = [0 for i in range(N)]#最適解リストの初期化
    for i in range(nlimit):#nlimit回、乱数生成
        rstep(p, N)
        weight = calcw(p,N)
        if weight <= weightlimit:
            value = calcval(p,N)
        else:
            value = 0
        if value > maxvalue:#最適解の更新
            maxvalue = value
            mweight = weight
            for j in range(N):#その時のp[]を最適解リストに代入
                bestp[j] = p[j]
    print(maxvalue, " ", mweight)
    print(bestp)

def calcw(p, N):
    """重量の計算"""
    w = 0
    for i in range(N):
        w += weights[i] * p[i]
    return w

def calcval(p,N):
    """評価値の計算"""
    v = 0
    for i in range(N):
        v += values[i] * p[i]
    return v

def rstep(p,N):
    """乱数による荷物の詰め合わせ"""
    for i in range(N):
        p[i] = int(random.random() * 2)



"""メイン実行"""
p = [0 for i in range(N)]#問題の答え
print(p)

print("practice")
for i in range(N):
    p[i] = int(random.random() * 2)
    print(p[i])


weightlimit = 250 #int(input("制限体重"))
#試行回数　何回乱数生成行うか
nlimit = 500 #int(input("試行回数"))
random.seed(SEED)

"""問題を解く
R回、実験の繰り返し"""
for i in range(R):
    solvekp(p, weightlimit, nlimit, N)
