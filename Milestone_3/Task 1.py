def intersection_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:

    i, j = 0, 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            i += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            if not result or result[-1] != list1[i]:
                result.append(list1[i])
            i += 1
            j += 1
    return result


def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:

    i, j = 0, 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

        result.extend(list1[i:])
        result.extend(list2[j:])
    return result


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8, 10]

print(intersection_sorted_lists(list1, list2))  # [2, 4, 6]
print(merge_sorted_lists(list1, list2))
