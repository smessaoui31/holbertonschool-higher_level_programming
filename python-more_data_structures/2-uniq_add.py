#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_num = set()
    total = 0
    for num in my_list:
        if num not in unique_num:
            unique_num.add(num)
            total += num
    return total
