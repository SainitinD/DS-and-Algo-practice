import heapq


# class Leaderboard:
#     def __init__(self):
#         self.curScore = {}  # Id => score
#
#     def addScore(self, playerId, score):
#         self.curScore[playerId] = score  # Time: O(1)
#
#     def reset(self, playerId):
#         self.curScore[playerId] = 0  # Time: O(1)
#
#     def top(self, k):
#         leaderboard = list(self.curScore.values())
#         leaderboard.sort(reverse=True)  # O(Nlog(N))
#         return sum(leaderboard[:k])  # TIME: O(Nlog(N)), Space: O(N) (decent solution but kinda slow)

class Leaderboard:
    def __init__(self):
        self.idToScore = {}

    def addScore(self, playerId, score):
        self.idToScore[playerId] = -score

    def reset(self, playerId):
        self.idToScore[playerId] = 0

    def top(self, k):
        leaderboard = list(self.idToScore.values())
        print(leaderboard)
        val = sum([heapq.heappop(leaderboard)])  # INCOMPLETE BUT FINISHED SOLUTION SHOULD BE => Time: O(log(N)???), Space: O(N)
        return val


    # Followup questions
    # Range of scores and ids


leaderboard = Leaderboard()
leaderboard.addScore(1, 73)  # leaderboard = [[1, 73]];
leaderboard.addScore(2, 56)  # leaderboard = [[1, 73], [2, 56]];
leaderboard.addScore(3, 39)  # leaderboard = [[1, 73], [2, 56], [3, 39]];
leaderboard.addScore(4, 51)  # leaderboard = [[1, 73], [2, 56], [3, 39], [4, 51]];
leaderboard.addScore(5, 4)  # leaderboard = [[1, 73], [2, 56], [3, 39], [4, 51], [5, 4]];
print(leaderboard.top(1))  # returns 73
leaderboard.reset(1)  # leaderboard = [[2, 56], [3, 39], [4, 51], [5, 4]];
leaderboard.reset(2)  ## leaderboard = [[3, 39], [4, 51], [5, 4]];
leaderboard.addScore(2, 51)  # leaderboard = [[2, 51], [3, 39], [4, 51], [5, 4]];
print(leaderboard.top(3))  # returns 141 = 51 + 51 + 39;
