def smallest_missing_positive_integer(nums):
    nums = [num for num in nums if num > 0]

    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if 0 <= index < len(nums) and nums[index] > 0:
            nums[index] = -nums[index]

    for i in range(len(nums)):
        if nums[i] > 0:
            return i + 1

    return len(nums) + 1





    



  

