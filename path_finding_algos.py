import heapq
from queue import Queue

def checkCycleInDAG(edges, n, s):
    adjNodes = {}
    visited_set = set()

    # Setup adjacent nodes list
    for node in range(1, n + 1):
        adjNodes[node] = []

    for edge in edges:
        adjNodes[edge[0]] = edge

    stack = [s]
    while stack:
        v = stack.pop()
        if v not in visited_set:
            for edge in adjNodes[v]:
                pass


# Network Delay Leetcode => https://leetcode.com/problems/network-delay-time/submissions/
def djikstra(times, n, k):
    # Overall Big-O (Priority queue based implementation)
    # Time: O (|E|log(|V|))
    # Space: O(V)

    visited = set()
    distance_map = {}
    # predecessor_map = {} (not needed for network delay)
    graph = {}

    # Time: O(|V|)
    for node in range(1, n + 1):
        graph[node] = []
       # predecessor_map[node] = None

    # Time: O(|E|)
    for edge in times:
        graph[edge[0]].append(edge)

    # TIME: O(|V|)
    for v in graph.keys():
        distance_map[v] = float("inf")

    distance_map[k] = 0
    # predecessor_map[k] = None

    # Time: O(|V|^2)
    queue = [[0, k]]
    heapq.heapify(queue)

    while len(queue) > 0:
        w, v = heapq.heappop(queue)
        # cur_visited = set(v)
        if v is not visited:
            visited.add(v)
            for v1, v2, w2 in graph[v]:
                new_cost = distance_map[v1] + w2
                if v2 not in visited and new_cost < distance_map[v2]:
                    distance_map[v2] = new_cost
                    # predecessor_map[v2] = v1
                    heapq.heappush(queue, [new_cost, v2])
    # print(distance_map)
    # print(predecessor_map)
    return -1 if float("inf") in distance_map.values() else max(distance_map.values())  # Time: O(|V|)


def max_area_of_island(grid):
    """
    BFS-Based solution. Technically works.
    :param grid:
    :return:
    """
    ROWS, COLS = len(grid), len(grid[0])

    def getAdjNodes(i, j):
        n1 = [i - 1, j]
        n2 = [i + 1, j]
        n3 = [i, j - 1]
        n4 = [i, j + 1]
        return [n1, n2, n3, n4]

    # Time: O(|V| * 4|V|) => O(|V|^2)
    def bfs(node):
        totalSum = 0
        queue = [node]
        while queue:
            i, j = queue.pop(0)  # Time: O(N)
            grid[i][j] = -1
            totalSum += 1
            for r, c in getAdjNodes(i, j):
                if 0 <= r < ROWS and 0 <= c < COLS:
                    if grid[r][c] == 1:
                        grid[r][c] = -1
                        queue.append([r, c])
        return totalSum

    totalSum = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                totalSum = max(totalSum, bfs([r, c]))

    return totalSum  # Time: O(|V|^2), Space: O(1)


def number_of_islands(grid):
    """
    BFS-Based solution. Technically Works. But takes too long to complete with a grid with a big island
    Hence, we solve this problem by using a DFS-Based solution.
    :type grid: List[List[str]]
    :rtype: int
    """
    # # Assuming, grid isn't required to be unchanged. We can use grid to act as visited.
    ROWS, COLS = len(grid), len(grid[0])

    def getAdjNodes(node):
        x, y = node
        adjN1 = [x + 1, y]
        adjN2 = [x - 1, y]
        adjN3 = [x, y + 1]
        adjN4 = [x, y - 1]
        return [adjN1, adjN2, adjN3, adjN4]

    # BFS using an array-based queue
    # def bfs(r, c):
    #     queue = [[r, c]]
    #     while queue:
    #         i, j = queue.pop(0)
    #         grid[i][j] = "-1"  # Visit node
    #         for adjNode in getAdjNodes([i, j]):
    #             x, y = adjNode
    #             if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == "1":
    #                 queue.append(adjNode)

    # BFS but with python queue package
    # def bfs_optim(r, c):
    #     # queue = queue.Queue() #  [[r, c]]
    #     queue = Queue()
    #     queue.put([r, c])
    #
    #     while not queue.empty():
    #         i, j = queue.get()
    #         grid[i][j] = "-1"  # Visit node
    #         for adjNode in getAdjNodes([i, j]):
    #             x, y = adjNode
    #             if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == "1":
    #                 queue.put(adjNode)

    # Dfs with recursion
    # Time Complexity: O(V*E) because of early pruning.
    # Else, Time complexity would be O(V^2 * E^2) if we didn't do the pruning
    def dfs(r, c):
        grid[r][c] = "-1"
        for adjNode in getAdjNodes([r, c]):
            x, y = adjNode
            if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == "1":
                dfs(x, y)

    total_islands = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1":
                #bfs(r, c)
                dfs(r,c)
                #bfs_optim(r, c)
                total_islands += 1

    # NOTE: Chose "-1" so that if we needed original grid, we just have to do a N^2 iteration to change "-1" to "1".

    return total_islands  # Time: O(|V|*|E|), Space: O(1) for DFS

def courseSchedule(numCourses, prerequisites):
    # Main idea is to check for cycles.
    # If there is a cycle (ie a => b and b => a), then we cannot finish

    prereqMap = {}
    for course in range(numCourses):
        prereqMap[course] = prereqMap.get(course, [])

    for prereq in prerequisites:
        a, b = prereq  # a => b (ie. before course 'a', you need to take course 'b')
        prereqMap[a].append(b)

    visited = set()
    active = set()

    def dfs(course):
        visited.add(course)
        output = True
        for prereqCourse in prereqMap[course]:
            if prereqCourse not in visited:
                active.add(prereqCourse)
                output = output and dfs(prereqCourse)
                active.remove(prereqCourse)
            else:
                if prereqCourse in active:
                    return False
        return output

    for course in range(numCourses):
        if course not in visited:
            active.add(course)
            if not dfs(course):
                return False
            active.remove(course)

    return True  # Time: O(|V| + |E|), Space: O(|V|) (where |V| is the num of courses)


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors


def cloneGraph(node):
    # Biggest problem was to figure out the inputs and the ouputs.
    # The input is the first node with adjacent lists
    # Then, use a dictionary to keep track of node, use dfs to create new nodes
    # if node is None:
    #     return None
    #
    # graph = {}
    # visited = set()
    #
    # def dfs(node):
    #     visited.add(node.val)
    #     newNode = graph[node.val]
    #
    #     for adjNode in node.neighbors:
    #         if adjNode.val not in visited:
    #             graph[adjNode.val] = Node(adjNode.val)
    #             dfs(adjNode)
    #         newNode.neighbors.append(graph[adjNode.val])
    #
    # # Create copy of first node and start dfs
    # graph[node.val] = Node(node.val)  # Remember, values are unique. So they can be used as keys
    # dfs(node)
    #
    # return graph[node.val]  # Time: O(|V| + |E|), Space: O(|V|)

    # More readable solution
    if node is None:
        return None

    graph = {}
    visited = set()

    def dfs(node, newNode):
        visited.add(node.val)

        for adjNode in node.neighbors:
            if adjNode.val not in visited:
                graph[adjNode.val] = adjNewNode = Node(adjNode.val)
                dfs(adjNode, adjNewNode)
            newNode.neighbors.append(graph[adjNode.val])

    graph[node.val] = newNode = Node(node.val)
    dfs(node, newNode)

    # Can't reduce space anymore (O(|V|)), Bc, if adjNode is already visited, then we need to get newAdjNode from graph
    return graph[node.val]  # Time: O(|V| + |E|), Space: O(2|V|) (bc of dfs recursion with two arguments) => O(|V|)

def swimInRisingWater(grid):
    # DFS based solution (simple solution) (Not very efficient)
    ROWS, COLS = len(grid), len(grid[0])

    def getAdjNodes(node):
        x, y = node
        adj1 = [x + 1, y]
        adj2 = [x - 1, y]
        adj3 = [x, y + 1]
        adj4 = [x, y - 1]
        return [adj1, adj2, adj3, adj4]

    visited = []

    def dfs(node):
        i, j = node
        if i == ROWS - 1 and j == COLS - 1: return True
        visited.append(node)
        for i, j in getAdjNodes(node):
            if 0 <= i < ROWS and 0 <= j < COLS and [i, j] not in visited and grid[i][j] <= time:
                if dfs([i, j]):
                    return True
        return False

    time = max(grid[0][0], grid[-1][-1])
    while True:
        if dfs([0, 0]):
            return time

        visited = []
        time += 1
    return time  # Time: O(|V| + |E|) (?? idk homie but prolly worse), Space: O(V^2)

def reconstructItinerary(tickets):
    # Create the adjacent list
    fromMap = {}
    for ticket in tickets:
        fAirport, tAirport = ticket
        fromMap[fAirport] = fromMap.get(fAirport, [])
        fromMap[fAirport].append(tAirport)

    # Sort the adjacent list
    for fAirport in fromMap.keys():
        fromMap[fAirport].sort()

    # Dfs
    def dfs(fAirport):
        returnString.append(fAirport)
        if len(visited) == len(fromMap.keys()) and len(active) == len(tickets):
            output = [x for x in returnString]
            return True
        visited.add(fAirport)
        for tAirport in fromMap[fAirport]:
            if tAirport not in active:
                active.append(tAirport)
                if dfs(tAirport):
                    return True
                active.remove(tAirport)
        returnString.remove(fAirport)
        return False

    visited = set()
    # active = ['JFK']
    active = 1
    returnString = []
    output = []
    for fAirport in fromMap.keys():
        if dfs(fAirport):
            return output

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

# print(findRedundantConnection([[1,5],[3,4],[3,5],[4,5],[2,4]]))





# Reconstruct Itinerary
tickets = [["JFK", "ATL"],["ATL", "MVH"], ["MVH", "ATL"], ["MVH", "SUH"], ["SUH", "JFK"], ["SUH", "MVH"], ["ATL", "SUH"]]
print(reconstructItinerary(tickets))

# Djikstra's call
# times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
# n = 3
# k = 2
# print(djikstra(times, n, k))

# Max Area of Island Call
# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,1,1,0,1,0,0,0,0,0,0,0,0],
#         [0,1,0,0,1,1,0,0,1,0,1,0,0],
#         [0,1,0,0,1,1,0,0,1,1,1,0,0],
#         [0,0,0,0,0,0,0,0,0,0,1,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# print(max_area_of_island(grid))

# Num of Islands Call
# grid = [["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0"],
#         ["1", "0", "1", "1", "1", "0", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
#         ["1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
#         ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]
#print(number_of_islands(grid))

# Course Schedule Call
# print(courseSchedule(2, [[1,0],[0,1]]))

# Swim in rising water call
# print(swimInRisingWater([[3,2],[0,1]]))