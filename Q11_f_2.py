def KetaSum(n):
    s = str(n)
    array = list(map(int, list(s)))
    return sum(array)

a = b = 1
count = 0
while count < 13:
    if (a % KetaSum(a)) == 0:
        print(a)
        count += 1
    i = a+b
    a = b
    b = i
