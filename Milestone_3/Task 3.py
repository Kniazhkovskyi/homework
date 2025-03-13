def shuffle_list(nums: list[int]) -> None:

    mid = (len(nums) + 1) // 2
    first_half, second_half = nums[:mid], nums[mid:]

    shuffled = []
    for i in range(len(second_half)):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])

    if len(first_half) > len(second_half):
        shuffled.append(first_half[-1])

    nums[:] = shuffled


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle_list(nums)
print(nums)
