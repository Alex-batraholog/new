my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
while n < len(my_list):
    if my_list[n] == 0:
        n += 1
        continue
    if my_list[n] < 0:
        break
    if my_list[n] > 0:
        print(my_list[n], end=' ')
        n += 1

list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
k = 0
while k < len(list):

