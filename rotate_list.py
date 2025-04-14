
# an example: [1, 2, 3, 4, 5], 3
# [3, 4, 5, 1, 2]
# shift_by = 5, same list
# shift_by = 6, same as shift_by = 1, 


########################Method 1##################
# TC: O(n*(k%n)), SC: O(1) 

def rotate_list_1(lst, shift_by):
    shift_by = shift_by % len(lst)
    for i in range(shift_by):
        rotate_list_once_right(lst)
    return lst

def rotate_list_once_right(lst):
    temp = lst[-1]
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    lst[0] = temp

print(rotate_list_1([1, 2, 3, 4, 5], 3))


#########Method 2: Double reverse#########################
#TC: O(n)   SC: O(1)


def rotate_list_2(list, shift_by):
    shift_by = shift_by % len(list)  
    reverse(list, 0, len(list) - 1)
    split_index = shift_by - 1
    reverse(list, 0, split_index)
    reverse(list, split_index + 1, len(list) - 1)
    return list

def reverse(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1

print(rotate_list_2([1, 2, 3, 4, 5], 3))