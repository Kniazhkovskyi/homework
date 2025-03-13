def EuclidNOD2(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def NODVSEH(nums: list[int]) -> int:
    result = nums[0]
    for num in nums[1:]:
        result = EuclidNOD2(result, num)
    return result


nums = [25, 35, 45, 75, 90]
print(NODVSEH(nums))
