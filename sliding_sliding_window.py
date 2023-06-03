# nums = [1, 1, 1, 0, 1, 1, 1, 0]
# k = 1


# def findMaxOnes(nums, k):
#     left, right = 0, 0
#     no_of_zeros = 0
#     maxRange = 0
#     while right < len(nums):
#         if nums[right] == 0:
#             no_of_zeros += 1
#
#         while no_of_zeros > k and left <= right:
#             if nums[left] == 0:
#                 no_of_zeros -= 1
#
#             left += 1
#         maxRange = max(maxRange, right - left + 1)
#         right += 1
#
#     if no_of_zeros > 0:
#         maxRange = max(maxRange, right - left + 1)
#     return maxRange
#
#
# print(findMaxOnes(nums, k))

nums = [1,1,1]
k = 5
def countSubarrays(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    sumScore = 0
    count = 0
    left, right = 0, 0
    while right < len(nums):
        sumScore += nums[right]

        while sumScore * (right - left + 1) >= k:
            # Reduce the window
            sumScore -= nums[left]
            left += 1

        if sumScore * (right - left + 1) < k:
            count += 1

        right += 1

    while sumScore > 0:
        sumScore -= nums[left]
        left += 1
        if left < right and sumScore * (right - left) < k:
            count += 1

    return count

print(countSubarrays(nums, 5))