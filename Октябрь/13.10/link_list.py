class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found_node = []
        node = self.head
        while node is not None:
            if node.value == val:
                found_node.append(node)
            node = node.next
        return found_node

    def delete(self, val, all=False):
        none = None
        if self.head is None:
            return
        while self.head and self.head.value == val:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            if not all:
                return
# Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
        while self.head:
            if self.head.value == val:
                none.next = self.head.next
                if self.head == self.tail:
                    self.tail = None
                if not all:
                    return
                self.head = self.head.next
            else:
                none = self.head
                self.head = self.head.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head = newNode
        else:
            if afterNode == self.tail:
                self.tail.next = newNode
                self.tail = newNode
            else:
                newNode.next = afterNode.next
                afterNode.next = newNode

    def read_list(self):
        result = []
        node = self.head
        while node is not None:
            result.append(node.value)
            node = node.next
        return result

n1 = Node(28)
n2 = Node(68)

s_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_tail(Node(256))
s_list.print_all_nodes()