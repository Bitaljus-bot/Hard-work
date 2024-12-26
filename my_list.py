my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start = len(my_list)
zero = 0
while zero < start:
    if my_list[zero] == 0:
        zero = zero + 1
        continue
    elif my_list[zero] > 0:
        print(my_list[zero])
        zero = zero + 1
    elif my_list[zero] < 0:
        break


