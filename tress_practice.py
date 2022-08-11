
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



n1 = TreeNode(0)
n2 = TreeNode(2)
root = TreeNode(1, n1, n2)

# # 4.5 Validate BST => Check if binary tree is binary search tree
# def validateBST(nodes):
#

#4.7 Build Order
# def findOrder(numCourses, prerequisites):
#     # Create the prereqMap
#     prereqMap = [[] for i in range(numCourses)]
#     visitedMap = [0 for i in range(numCourses)]
#     for prereq in prerequisites:
#         prereqMap[prereq[0]].append(prereq[1])
#
#     for i, n in enumerate(prereqMap):
#         print(f'{i} => {n}')
#
#
# def dfs(node):
#     if not node: return
#
#     stack = []
#     while len(stack):
#         n = stack.pop()
#         visitedMap[n] = 1
#         for adjNode in prereqMap[n]:
#             stack.append(adjNode)

# def build_order(list_of_projects, list_of_dependencies):
#
#     # Create the dependency map
#     dependency_map = {}
#     for dependency in list_of_dependencies:
#         if dependency_map.get(dependency[1], -1) == -1:
#             dependency_map[dependency[1]] = []
#         dependency_map[dependency[1]].append(dependency[1])
#
#     def dfs(root):
#

def findRedundantConnection(edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    sets = {}  # root => set

    # create sets for each node
    # Time: O(E*V)
    # for edge in edges:
    #     if edge[0] not in sets.keys():
    #         sets[edge[0]] = set()
    #     if edge[1] not in sets.keys():
    #         sets[edge[1]] = set()

    sets = {}
    for n in range(1, len(edges) + 1):
        sets[n] = set()

    # Time: O(E*V)
    def getRootEdge(node):
        for root in sets.keys():
            rootSet = sets[root]
            if node == root or node in rootSet:
                return root

    # Time: O(E^2*V)
    for edge in edges:
        isVertex1RootNode = getRootEdge(edge[0])
        isVertex2RootNode = getRootEdge(edge[1])

        if isVertex1RootNode == isVertex2RootNode:
            return edge
        else:
            # combine unique sets
            sets[isVertex1RootNode] = sets[isVertex1RootNode].union(sets[isVertex2RootNode])
            sets.pop(isVertex2RootNode)
            sets[isVertex1RootNode].add(isVertex2RootNode)

print(findRedundantConnection([[1,5],[3,4],[3,5],[4,5],[2,4]]))