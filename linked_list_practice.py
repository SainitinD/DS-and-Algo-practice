class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.length = 0 if not node else 1

    def append(self, newNode):
        if not self.head:
            self.head = newNode
        else:
            node = self.head
            while node.next:
                node = node.next

            node.next = newNode
        self.length += 1

    # def append(self, newNode, index):
    #     if index >= self.length:
    #         raise IndexError("Index is greater than length of array")
    #
    #     idx = 0
    #     node = self.head
    #     while node.next:
    #         if idx + 1 == index:
    #             nextNode = node.next
    #             node.next = newNode
    #             newNode.next = nextNode
    #             break
    #         else:
    #             node = node.next
    #             idx += 1
    #
    #     self.length += 1

    def delete(self, index):
        if index >= self.length:
            raise IndexError()

        # Handle head node's deletion
        if index == 0:
            val = self.head.val
            self.head = self.head.next
            self.length -= 1
            return val

        # Handle any other node's deletion
        idx = 1
        prevNode = self.head
        curNode = self.head.next

        while idx < index:
            prevNode = curNode
            curNode = curNode.next
            idx += 1

        val = curNode.val
        prevNode.next = curNode.next
        self.length -= 1
        return val

    # Q1 Delete duplicates
    # Input:  [1, 2, 2, 1]
    # Output: [1, 2]
    def deleteDuplicates(self):
        # buffer = {}
        #
        if self.length <= 1:
            return
        #
        # prevNode = self.head
        # curNode = self.head.next
        #
        # buffer[prevNode.val] = True
        # while curNode:
        #     if buffer.get(curNode.val, False):
        #         prevNode.next = curNode.next
        #         curNode = curNode.next
        #         self.length -= 1
        #     else:
        #         buffer[curNode.val] = True
        #         prevNode = curNode
        #         curNode = curNode.next
        # Space: O(N), Time: O(N)

        # TODO: Solve the problem with O(1) Space
        # prevNode = self.head
        # curNode = self.head.next
        # immNext = curNode
        # while prevNode:
        #     prevNode = immNext
        #     if prevNode.next:
        #         immNext = prevNode.next
        #         curNode = prevNode.next
        #     tempPrev = prevNode
        #     while curNode:
        #         if prevNode.val == curNode.val:
        #             tempPrev.next = curNode.next
        #             curNode = curNode.next
        #         else:
        #             tempPrev = curNode
        #             curNode = curNode.next
        #     if prevNode.next:
        #         prevNode = immNext
        #         curNode = immNext.next

    def findKthToLast(self, k):
        # Assuming length property is not given
        if not self.head:
            raise IndexError

        if not self.head.next and k == 1:
            return self.head.val

        length = 1
        node = self.head.next
        while node:
            node = node.next
            length += 1

        if length < k:
            raise IndexError(f"The Linked List length is {length} while request kth value is {k}.\n"
                             + "\t\t\tReduce the kth value in the bounds of the llist ds.")

        if length == k:
            return self.head.val

        idxToFind = length - k

        node = self.head.next
        idx = 1
        while idx < idxToFind:
            node = node.next
            idx += 1

        return node.val

    def __len__(self):
        return self.length

    def _toString(self):
        result = "["
        if not self.length:
            return result + "]"

        if self.length == 1:
            return result + str(self.head) + "]"

        node = self.head
        while node:
            result = result + str(node) + ", "
            node = node.next
        result = result[:-2] + "]"
        return result

    def __str__(self):
        result = "["
        if not self.length:
            return result + "]"

        if self.length == 1:
            return result + str(self.head) + "]"

        node = self.head
        while node:
            result = result + str(node) + ", "
            node = node.next
        result = result[:-2] + "]"
        return result

# Test Cases
n1 = Node(1231, None)
n2 = Node(12412, None)
n3 = Node(5942, None)
n4 = Node(15, None)

linkedList = LinkedList()
linkedList.append(n1)
linkedList.append(n2)
linkedList.append(n3)
linkedList.append(n4)
print(linkedList)
# linkedList.deleteDuplicates()

print(linkedList.findKthToLast(4))
