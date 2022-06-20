from errors import EmptyStackException


class Stack:
    def __init__(self):
        self.array = []
        self.top = None

    def pop(self):
        if len(self.array) == 0:
            raise EmptyStackException("Stack is empty. Add a value before popping values")

        item = self.array.pop()
        self.top = self.array[-1]
        return item

    def push(self, item):
        self.array.append(item)
        self.top = item

    def peek(self):
        if not self.top:
            raise EmptyStackException("Stack is empty. Add a value before peeking")
        return self.top

    def isEmpty(self):
        return len(self.array) == 0

    def __len__(self):
        return len(self.array)

    def __str__(self):
        result = "["
        for i in range(len(self) - 1, -1, -1):
            result = result + f"{self.array[i]}, "
        result = result[:-2] + "]"
        return result


# Q2. Stack Min => Get the Min element on the stack in O(1) time.
class Stack2:
    def __init__(self):
        self.array = []
        self.top = None

    def pop(self):
        if len(self.array) == 0:
            raise EmptyStackException("Stack is empty. Add a value before popping values")

        item = self.array.pop()
        self.top = self.array[-1][0]
        return item

    def push(self, item):
        if len(self.array) == 0:
            self.array.append((item, item))
            self.top = item
            return
        else:
            minVal = self.array[-1][1]
            newMinVal = minVal if minVal < item else item
            self.array.append((item, newMinVal))
            self.top = item

    def peek(self):
        if not self.top:
            raise EmptyStackException("Stack is empty. Add a value before peeking")
        return self.top

    def isEmpty(self):
        return len(self.array) == 0

    def min(self):
        return self.array[-1][1]

    def __len__(self):
        return len(self.array)

    def __str__(self):
        result = "["
        for i in range(len(self) - 1, -1, -1):
            result = result + f"{self.array[i]}, "
        result = result[:-2] + "]"
        return result


# stack = Stack2()
# stack.push(1)
# stack.push(2)
# stack.push(-1)
# print(stack)
# print(stack.min())
# stack.pop()
# print(stack)
# print(stack.min())
# stack.push(4)
# stack.push(-2)
# print(stack)
# print(stack.min())


# Q1 Implement three stacks using one array
class Stack1:
    def __init__(self, noOfStacks):
        self.array = []
        self.top1 = None
        self.top2 = None
        self.top3 = None
        self.noOfStacks = noOfStacks
        self.stack1Length = 0
        self.stack2Length = 0
        self.stack3Length = 0
        self.totalElements = 0

    # private elements to be used to help these values.
    def _getStackLength(self, stackNum):
        if stackNum == 0:
            return self.stack1Length
        elif stackNum == 1:
            return self.stack2Length
        else:
            return self.stack3Length

    def _setStackTopVal(self, stackNum, val):
        if stackNum == 0:
            self.top1 = val
        elif stackNum == 1:
            self.top2 = val
        else:
            self.top3 = val

    def _incStackLength(self, stackNum):
        if stackNum == 0:
            self.stack1Length += 1
        elif stackNum == 1:
            self.stack2Length += 1
        else:
            self.stack3Length += 1

    def _decStackLength(self, stackNum):
        if stackNum == 0:
            self.stack1Length -= 1
        elif stackNum == 1:
            self.stack2Length -= 1
        else:
            self.stack3Length -= 1

    def push(self, stackNum, item):
        # Calculate index to add value at based on stackNo and no.of values in that stack
        curIdx = self.noOfStacks * self._getStackLength(stackNum) + stackNum

        # Add empty 0 values until we reach the designated idx location
        while self.totalElements < curIdx:
            self.array.append(0)
            self.totalElements += 1

        self.array[curIdx] = item
        self.array.append(item)

        # Sets the top value for the designated stack
        self._setStackTopVal(stackNum, item)

        # Up the length of the designated stack
        self._incStackLength(stackNum)

    def pop(self, stackNum):
        if len(self.array) == 0:
            raise EmptyStackException("Stack is empty. Add a value before popping values")

        curIdx = self.noOfStacks * self._getStackLength(stackNum) + stackNum
        item = self.array.pop(curIdx)

        # decrease stack length
        self._decStackLength(stackNum)
        self.totalElements -= 1

        newTopIdx = self.noOfStacks * self._getStackLength(stackNum) + stackNum
        self._setStackTopVal(stackNum, self.array[newTopIdx])
        return item

    def peek(self, stackNum):
        if not self.totalElements:
            raise EmptyStackException("Stack is empty. Add a value before peeking")
        if stackNum == 0:
            return self.top1
        elif stackNum == 1:
            return self.top2
        else:
            return self.top3

    def isEmpty(self):
        return len(self.array) == 0

    def __len__(self):
        return len(self.array)

    # def __str__(self):
    #     result = "["
    #     for i in range(0, len(self.array)):
    #         result = result + f"{self.array[i]}, "
    #     result = result[:-2] + "]"
    #     return result


# Q4 Implement Queue using two stacks.
# Good reference video => https://www.youtube.com/watch?v=AN0axYeLue0
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.length = None

    def __len__(self):
        return len(self.s1) + len(self.s2)

    def push(self, item):
        self.s1.append(item)

    def pop(self):
        if len(self) == 0:
            return
        if not len(self.s2):
            while len(self.s1):
                val = self.s1.pop()
                self.s2.append(val)
            return self.s2.pop()
        else:
            return self.s2.pop()

    def peek(self):
        if len(self) == 0:
            return

        if not len(self.s2):
            while len(self.s1):
                val = self.s1.pop()
                self.s2.append(val)
            return self.s2[-1]
        else:
            return self.s2[-1]

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        result = "["
        # while len(self.s2) > 0:
        #     result = result + f"{self.s2.pop()}, "
        # while len(self.s1) > 0:
        #     result = result + f"{self.s1.pop()}, "
        for i in range(len(self.s2) - 1, - 1, -1):
            result = result + f"{self.s2[i]}, "
        for i in range(0, len(self.s1)):
            result = result + f"{self.s1[i]}, "
        result = result[:-2] + "]"
        return result

# Q4 test cases
# queue = MyQueue()
# queue.push(1)
# queue.push(2)
# queue.push(3)
# print(queue)
# print(queue.peek())
# queue.pop()
# print(queue)
# print(queue.peek())
# queue.push(4)
# queue.push(5)
# queue.push(6)
# print(queue)
# print(queue.peek())
# queue.pop()
# queue.pop()
# print(queue)
# print(queue.peek())
# print(queue)
# print(queue.isEmpty())