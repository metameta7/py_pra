# cording: utf-8

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high ) // 2 #midの更新するってとこがポイント
        if list[mid] == item:
            print('Found')
            return mid
        if list[mid] > item:
            high = mid -1 #midより右側もういらん
        else:
            low = mid + 1 #midより左側もういらん
    return None

test_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(binary_search(test_list,10))
