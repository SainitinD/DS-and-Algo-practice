def house_robber(nums):
    # Idea: house robber can rob any house as long as one away from previously robbed house
    # Algo Time: O(N^2)??, Space: O(N)
    mem = [0 for i in range(len(nums))]

    # Time: O(N^2)
    for i in range(len(nums)):
        if i < 2:
            mem[i] = nums[i]
        else:
            for j in range(i - 1):
                if nums[i] + mem[j] > mem[i]:
                    mem[i] = nums[i] + mem[j]
    return max(mem)

    # Write the algo with Time: O(N) and Space: O(1) (See leetcode starred)


def min_climbing_stairs(costs):
    dp = []
    if len(costs) == 0:
        return 0
    elif len(costs) == 1:
        return costs[1]

    for i in range(len(costs)):
        if i < 2:
            dp.append(0)
        elif i == 2:
            dp.append(min(costs[0], costs[1]))
        else:
            if costs[i - 1] + dp[-1] <= costs[i - 2] + dp[-2]:
                dp.append(costs[i - 1] + dp[-1])
            else:
                dp.append(costs[i - 2] + dp[-2])

    print(dp)
    print(costs)
    return dp[-1]


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    # Greedy Solution => Time: O(N^2), Space: O(1)
    # My boy, Timothy H Chang's Solution
    def check_if_palindrome(l, r):
        if 0 <= l and r < len(s):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r
        else:
            return l, r

    res = ""
    for i in range(len(s)):
        # Check for odd palindromes
        l, r = check_if_palindrome(i, i)
        if r - l > len(res):
            res = s[l:r]  # Store substring from l to r(not included)
        # Check for even palindromes
        l, r = check_if_palindrome(i, i + 1)
        if r - l > len(res):
            res = s[l:r]  # Store substring from l to r(not included)
    return res

    # # TODO: Write the dynamic programing solution for this (this will prolly take 2D array but there might be a 1D array sol)
    # # Rows => starting index of substring, Columns => ending index of substring (inclusive)
    # palindromeDP = [[0 for i in range(len(s))] for j in range(len(s))]
    #
    # # Basecase: greatest palindrome = 1, for each character.
    # for i in range(len(s)):
    #     palindromeDP[i][i] = True
    #
    # # Basecase: when left > right, we can't make a substring (ie. make it false)
    # # Already set in Preinitialization


def knapsackUnbounded(cap, v, w):
    dp = [0 for i in range(cap + 1)]
    for j in range(len(v)):
        for i in range(1, cap + 1):
            if w[j] <= i:
                dp[i] = max(dp[i], dp[i - w[j]] + v[j])

    # recurrence relation: value at current_capacity or current value + value at (current_capacity - curValue's capacity)
    return dp[-1]


def coinChange(coins, amount):
    # This is a type of knapsack unbounded problem where we are trying to optimize
    # for least num of coins needed to reach target amount.
    # In this problem, the indices represent the amount
    # TODO: Review what the indices mean in dp in this problem.

    # Helpful Tips
    #   => Trick is that instead of subtracting weights, we subtract value from amount index.
    # 	=> Also, as we are trying to find the minimum value, we should start with "inf" in the dp and
    #      use 'min' instead of 'max'

    # 1. Bottom-up approach (I think??)
    # Choose 10001 because 10000 seems to the limit for amount.
    # If amount's upper-limit is ambigious, I would choose float("inf") (positive infinity).
    # dp = [10001 for i in range(amount + 1)]
    # dp[0] = 0
    #
    # for i in range(len(coins)):
    #     for j in range(1, amount + 1):
    #         if coins[i] <= j:
    #             dp[j] = min(dp[j], 1 + dp[j - coins[i]])
    #
    # print(dp)
    # return -1 if dp[-1] > 10000 else dp[-1]  # Time: O(len(coins)*amount), Space: O(amount+1)

    # 2. But, I prefer this haha. Another Bottom-up solution with better variable names
    dp = [float("inf") for i in range(amount + 1)]
    dp[0] = 0

    # Switch from 'indexed for-loop' to 'enhanced for-loop' as we don't need indices for coins (we only need coin vals)
    for coin in coins:
        for j in range(1, amount + 1):
            if coin <= j:
                dp[j] = min(dp[j], 1 + dp[j - coin])

    return -1 if dp[-1] == float("inf") else dp[-1]  # Time: O(len(coins)*amount), Space: O(amount+1)


def maxProductSubarray(nums):
    # dp = [[0 for r in range(len(nums)+1)] for c in range(len(nums)+1)]
    # # type of longest common substring problem
    # # row of dp is the starting index of substring, col of dp is the ending index of substring (inclusive)
    #
    # # Basecase 1: if rowIdx < colIdx, we will have an invalid substring. So max product should be 0 (Taken care of)
    # # basecase 2: if r == c, set dp[r][c] = nums[r] (the value at that index)
    # for r in range(1, len(nums)+1):
    #     for c in range(1, len(nums)+1):
    #         if r == c:
    #             dp[r][c] = nums[c-1]
    #
    # # handle recurrence
    # res = -(float("inf"))
    # for r in range(1, len(nums)+1):
    #     for c in range(r+1, len(nums)+1):
    #         dp[r][c] = dp[r][c-1] * nums[c-1]
    #
    # for r in range(1, len(nums)+1):
    #     for c in range(r, len(nums)+1):
    #         res = max(res, dp[r][c])
    #
    # return res  # Time: O(N^2), Space: O(N^2) => Solution works, but its too slow


    dpVal = 0
    # type of longest common substring problem
    # row of dp is the starting index of substring, col of dp is the ending index of substring (inclusive)

    # Basecase 1: if rowIdx < colIdx, we will have an invalid substring. So max product should be 0 (Taken care of)
    # basecase 2: if r == c, set dp[r][c] = nums[r] (the value at that index)
    # for r in range(1, len(nums)+1):
    #     for c in range(1, len(nums)+1):
    #         if r == c:
    #             dp[r][c] = nums[c-1]

    # handle recurrence
    res = -(float("inf"))
    for r in range(1, len(nums)+1):
        dpVal = nums[r-1]
        res = max(res, dpVal)
        for c in range(r+1, len(nums)+1):
            dpVal = dpVal * nums[c-1]
            res = max(res, dpVal)

    # for r in range(1, len(nums)+1):
    #     for c in range(r, len(nums)+1):
    #         res = max(res, dp[r][c])

    return res  # Time: O(N^2), Space: O(1) => Solution works and takes constant space, but its too slow


def climbingStairs(n):
    # dp = [0 for i in range(n + 1)]
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # elif n == 2:
    #     return 2
    #
    # dp[0] = 0
    # dp[1] = 1
    # dp[2] = 2
    #
    # for i in range(3, n + 1):
    #     dp[i] = dp[i - 1] + dp[i - 2]
    #
    # return dp[-1]  # Time: O(N), Space: O(1)

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    two_step, one_step = 1, 2

    for i in range(3, n + 1):
        res = one_step + two_step
        two_step = one_step
        one_step = res

    return one_step  # Time: O(N), Space: O(1)





# print(house_robber([1,2,3,1]))
# print(min_climbing_stairs([1,100,1,1,1,100,1,1,100,1]))
# print(longestPalindrome("babad"))
# print(targetSum([1, 0], 2))

# capacity = 7
# values = [6]
#
# values1 = [1,2,5]
# capacity1 = 11
#
# values2 = [1]
# values3 = 10000
# print(coinChange(values2, values3))

#print(maxProductSubarray([1,-2,-2,3,4,5,6]))

print(climbingStairs(15))