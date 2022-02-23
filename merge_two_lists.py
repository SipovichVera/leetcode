list1 = [1, 1, 2, 3, 4, 6, 9]
list2 = [9, 7, 6, 2, 2, 1]

def merge_lists(list1, list2):
    sort_list(list1)
    sort_list(list2)
    list = []
    index1 = 0
    index2 = 0
    while index1 < len(list1) or index2 < len(list2):
        if list1[index1] < list2[index2]:
            list.append(list1[index1])
            index1 += 1
        if list2[index2] < list1[index1]:
            list.append(list2[index2])
            index2 += 1
        else:
            list.append(list1[index1])
            list.append(list2[index2])
            index2 += 1
            index1 += 1
    return list


def sort_list(list):
    return list.sort()

print(merge_lists(list1, list2))
