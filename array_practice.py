# Madhava's hackerrank practice

arr = ["Daisy+++", "Rose++++", "Hyacinth", "Poppy+++"]

# ['Daisy+++', 'Rose++++', 'Hyacinth', 'Poppy+++']
#
# def sol(arr):
#     totalLen = 0
#     for s in arr: totalLen += len(s)
#
#     maxStrLen = len(max(arr, key=len))
#     print(maxStrLen)
#
#     # Pre-processing step => Time: O(n*x)
#     for i in range(len(arr)):
#         for j in range(len(arr[i]), maxStrLen):
#             newW = arr[i] + "+"
#             arr[i] = newW
#     print(arr)
#
#     # If x = len(maximum string), n = len(arr) => Space: O(x * n)
#     res = [0 for i in range(totalLen)]
#     idxTracker = [0 for i in range(len(arr))]  # [3,2,2,2]
#
#     for i in range(len(res)):  # => 4 => 4 % 4 => 0
#         print(res)
#         strNum = i % len(arr)  # 0
#         charCurIdx = idxTracker[strNum]  # 0
#         res[i] = arr[strNum][charCurIdx]
#         idxTracker[strNum] += 1
#         # idxTracker +=
#
#     resF = ""
#     for v in res:
#         if v is not '+':
#             resF += v
#     return resF


# print(sol(arr))

# Capital One => Codesignal (Two SUM modification)
queries = ["+4", "+5", "+1", "-4", "+1"]
diff = 1
numbers = []

for c in queries:
    sign = c[0]
    num = int(c[-1])
    if sign is "-":
        numbers.remove(num)
    else:
        numbers.append(num)

hashM = {}
total = 0
for i, n in enumerate(numbers):
    if n - diff in hashM.keys():
        total += hashM[n - diff]
    else:
        hashM[n - diff] = hashM.get(n - diff, 0) + 1


print(numbers)
print(total)
