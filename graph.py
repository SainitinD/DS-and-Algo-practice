class GraphNode:
    def __init__(self, value=None, edges=[], visited=False):
        self.value = value
        self.edges = edges
        self.visited = visited

    def add_edge(self, edge_list):
        for e in edge_list:
            self.edges.append(e)

    def clear_visited(self):
        self.visited = False
        self.visited = False


class GraphAlgorithm:
    def __init__(self):
        self.DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.visited = set()

    # Assume graph will be in the format of 2D list
    def bfs(self, root, graph):
        ROWS, COLS = len(graph), len(graph[0])
        visited = set()
        queue = [root]
        while len(queue):
            r, c = queue.pop(0)
            if (r, c) not in visited:
                visited.add((r, c))

                # Add node's adjacent nodes into the graph
                for i, j in self.DIRECTIONS:
                    new_r, new_c = r + i, c + j
                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and [new_r,new_c] not in visited:
                        queue.append([new_r, new_c])

                print(graph[r][c], (r, c))

    def bfs_with_node(self, rootNode):
        visited = set()
        queue = [rootNode]
        while len(queue):
            node = queue.pop(0)
            visited.add(node.value)
            for e in node.edges:
                if e.value not in visited:
                    print(f"parent node: {node.value}, child node: {e.value}")
                    queue.append(e)
            # print(node.value)


    def getAdjNodes(self, node):
        x,y = node
        adjN1 = [x+1, y]
        adjN2 = [x-1, y]
        adjN3 = [x,y+1]
        adjN4 = [x,y-1]
        return [adjN1, adjN2, adjN3, adjN4]

    def dfs(self, node):
        if node in self.visited:
            return
        i,j = node
        self.visited.add(node)
        self.grid[i][j] = -1
        for adjNode in self.getAdjNodes(node):
            if adjNode not in self.visited:
                self.dfs(adjNode)


nodeA = GraphNode(value="A")
nodeB = GraphNode(value="B")
nodeC = GraphNode(value="C")
nodeD = GraphNode(value="D")
nodeE = GraphNode(value="E")
nodeF = GraphNode(value="F")
nodeG = GraphNode(value="G")
nodeH = GraphNode(value="H")
nodeI = GraphNode(value="I")
nodeJ = GraphNode(value="J")


# Issue: For some reason, all of the nodes are being added to the A's edgeList (:')
nodeA.add_edge([nodeB, nodeD])
nodeB.add_edge([nodeI, nodeC])
nodeD.add_edge([nodeJ, nodeE, nodeF])
nodeF.add_edge([nodeG])
# nodeI.add_edge([nodeB])
# nodeC.add_edge([nodeB])
# nodeE.add_edge([nodeD])
# nodeJ.add_edge([nodeJ])
# nodeG.add_edge([nodeF])

matrix = [[1, 2, 3, 4],
          [2, 3, 4, 5],
          [3, 4, 5, 6],
          [4, 5, 6, 7]]

# 10
# [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
# 7
# 5

graphDoer = GraphAlgorithm()
graphDoer.bfs([0, 0], matrix)
# graphDoer.bfs_with_node(nodeA)


