#
# class TreeNode:
#     def __init__(self, val=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
#
# n1 = TreeNode(0)
# n2 = TreeNode(2)
# root = TreeNode(1, n1, n2)
#
# # # 4.5 Validate BST => Check if binary tree is binary search tree
# # def validateBST(nodes):
# #
#
# #4.7 Build Order
# # def findOrder(numCourses, prerequisites):
# #     # Create the prereqMap
# #     prereqMap = [[] for i in range(numCourses)]
# #     visitedMap = [0 for i in range(numCourses)]
# #     for prereq in prerequisites:
# #         prereqMap[prereq[0]].append(prereq[1])
# #
# #     for i, n in enumerate(prereqMap):
# #         print(f'{i} => {n}')
# #
# #
# # def dfs(node):
# #     if not node: return
# #
# #     stack = []
# #     while len(stack):
# #         n = stack.pop()
# #         visitedMap[n] = 1
# #         for adjNode in prereqMap[n]:
# #             stack.append(adjNode)
#
# # def build_order(list_of_projects, list_of_dependencies):
# #
# #     # Create the dependency map
# #     dependency_map = {}
# #     for dependency in list_of_dependencies:
# #         if dependency_map.get(dependency[1], -1) == -1:
# #             dependency_map[dependency[1]] = []
# #         dependency_map[dependency[1]].append(dependency[1])
# #
# #     def dfs(root):
# #

def threesum(nums):
    nums.sort()
    res = []
    for i in range(1,len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = len(nums)-1
        while j < k:
            s = nums[i]+nums[j]+nums[k]
            if s > 0:
                k -= 1
            elif s < 0:
                j += 1
            else:
                res.append([nums[i],nums[j],nums[k]])
                j += 1
                while nums[j-1]==nums[j] and j<k:
                    j += 1
    return res
val = [-1,0,1,2,-1,-4]
print(threesum(val))
