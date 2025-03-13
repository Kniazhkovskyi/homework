from typing import List, Tuple


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:

    seen = {}
    for i, num in enumerate(li):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i


print(find_sum_fast(5, [1, 2, 3, 4, 5]))
print(find_sum_fast(8, [3, 5, 2, 8, 1, 7]))

# Временная сложность: O(n)
# Пространственная сложность: O(n)
