def move_zeroes(nums: list[int]) -> None:

    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]
move_zeroes(nums)
print(nums)
