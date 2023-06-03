n = [100, 200, 100, 400, 500, 2, 600]


def sliding_window_brute_force(k):
    max_sum = 0
    for i in range(0, len(n) - k + 1):
        cur_sum = 0
        for j in range(0, k):
            cur_sum = cur_sum + n[i + j]

        max_sum = max(max_sum, cur_sum)
    return max_sum


def sliding_window(k):
    """
    Create a sliding window of fixed 'k' size.
    :param k:
    :return:
    """
    max_sum = 0
    for i in range(0, k):  # Create initial sum from the window!!!!
        max_sum += n[i]

    # window_sum = max_sum
    # for i in range(k, n):
    #     window_sum = window_sum - n[i] + n[i+k]
    #     max_sum = max(max_sum, window_sum)
    # return max_sum

    window_sum = max_sum
    for i in range(k, len(n)):
        window_sum = window_sum + n[i] - n[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum  # Time: O(N), Space: O(1)


# print(sliding_window(5))

# Easy to Understand solution
def maximum_consequetive_ones(inp):
    max_range = 0
    no_of_zeros = 0
    l, r = 0, 0
    while r < len(inp):
        # Expand the window
        if inp[r] == 0: no_of_zeros += 1
        r += 1

        # Check for the condition
        while no_of_zeros >= 2:
            max_range = max(max_range, r - l)  # This works. Why? Think about it!
            if inp[l] == 0: no_of_zeros -= 1
            l += 1

    # Edge case: When the longest consecutive numbers are at the end!
    if no_of_zeros < 2:
        max_range = max(max_range, r - l - 1)
    return max_range

# My solution. It has the same efficiency but its hard to understand
#     max_range = 0
#     sliding_window = []
#     no_of_zeroes = 0
#     l, r = 0, 0
#     while l <= r < len(inp):
#         if inp[r] == 0 and no_of_zeroes + 1 > 1:
#             max_range = max(max_range, len(sliding_window))
#             sliding_window.pop(0)
#             if inp[l] == 0: no_of_zeroes -= 1
#             l += 1
#             continue
#         sliding_window.append(inp[r])
#         if inp[r] == 0: no_of_zeroes += 1
#         r += 1
#
#     return max_range


inp = [1, 0, 0]
print(maximum_consequetive_ones(inp))
