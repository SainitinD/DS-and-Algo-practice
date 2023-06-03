class customDict:
    def __init__(self):
        self.data = {}
        self.keyOffset = 0
        self.valOffset = 0

    def get(self, k):
        return self.data.get(k - self.keyOffset) + self.valOffset

    def add_to_key(self, val):
        self.keyOffset += val

    def add_to_val(self, val):
        self.valOffset += val

    def insert(self, key, val):
        self.data[key] = val


cD = customDict()
queryType = ["insert", "insert", "addToValue", "addToKey", "get"]
query = [[1, 2], [2, 3], [2], [1], [3]]

res = 0
for qT, q in zip(queryType, query):
    if qT == "insert":
        cD.insert(q[0], q[1])
    elif qT == "addToValue":
        cD.add_to_val(q[0])
    elif qT == "addToKey":
        cD.add_to_key(q[0])
    else:
        res += cD.get(q[0])

print(cD.data)
print(res)
print(isinstance(cD, customDict))