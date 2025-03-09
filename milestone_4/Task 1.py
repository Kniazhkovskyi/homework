from typing import List, Tuple


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:

    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return i, j


print(find_sum(5, [1, 2, 3, 4, 5]))
print(find_sum(8, [3, 5, 2, 8, 1, 7]))

# Временная сложность: O(n^2)
# Пространственная сложность: O(1)
