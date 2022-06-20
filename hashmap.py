class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def push(self, new_node):
        if not self.head: self.head = new_node
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

class HashMap:
    def __init__(self):
        pass

