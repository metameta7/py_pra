import itertools

male = list("1" * 4)
female = list("0" * 2)

print(male)
print(female)

ori = male + female
print(ori)

'''
p = list(itertools.permutations(ori));
print(p)
'''





'''
#http://pythonista.hateblo.jp/entry/A009

import itertools

#p = list('MMMMMMMMMMMMMMMMMMMMFFFFFFFFFF')
p = list("MMMMFF")
#r=30
r = 6
cnt = 0

for q in set(itertools.permutations(p,r)):
    #for n in range (2, 28):
    for n in range (2, 28):
        former = q[:n]
        latter = q[n:]
        if former.count('M') != former.count('F') or latter.count('M') != latter.count('F'):
            cnt += 1
print cnt
'''




'''
模範解答では、男女の順列の問題を2次元の表を使って考えている。
男性が来たら右へ、女性が来たら上へ移動する経路を考える。
男女が同数になる場所をカウントしないように、経路が何通りあるかを算出する。
'''
def path(b, g):
    if b == g:
        return 0
    elif b - g == 9:
        return path(b-1, g)
    elif b == 0 or g == 0:
        return 1
    else:
        return path(b-1, g) + path(b, g-1)

print (path(6,2))





'''



zero = [0]
m = [0,1,1,1,1]
print(zero + m )

female = [0,1,1]

f_0 = [0,1,1,1,1]
f_1 = [1,1,1,1,1]
f_2 = [1,1,1,1,1]


f_1[1] = f_1[0] + f_0[1]
f_1[2] = f_1[1] + f_0[2]
f_1[3] = f_1[2] + f_0[3]
f_1[4] = f_1[3] + f_0[4]
f_1 = [f_1[0], f_1[1],f_1[2],f_1[3],f_1[4]]

f_2[1] = f_2[0] + f_1[1]
f_2[2] = f_2[1] + f_1[2]
f_2[3] = f_2[2] + f_1[3]
f_2[4] = f_2[3] + f_1[4]



print(f_1)
print(f_2)

x = [1,2,3,4,5]
for i in range(1,len(x)):
    print(i)
    t_i = [i, i+1]
    print(t_i)
    print(t_i[0])



'''

f_i[i] = f_i[i-1] + f_i-0[1]
f_1[2] = f_1[1] + f_0[2]
f_1[3] = f_1[2] + f_0[3]
f_1[4] = f_1[3] + f_0[4]
f_1 = [f_1[0], f_1[1],f_1[2],f_1[3],f_1[4]]
'''


a,b,c,d,e,f,g,h = range(8)
oG0 = [[b,c,d,e,f],[c,e],[d],[e],[f],[c,g,h],[f,h],[f,g]]


def set_unvisited(G):
    vstate = []
    for vertex in range(len(G)):
        vstate.append(None)
    return vstate

states = set_unvisited(oG0)
def DFS(G,start):
    states[start] = True
    print(start)
    for u in G[start]:
        if not states[u]:
            DFS(G,u)

print(DFS(oG0,a))
