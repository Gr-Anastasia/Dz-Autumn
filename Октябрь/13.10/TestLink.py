from link_list import Node, LinkedList


class TestLL:
    ll = LinkedList()
    ll.add_in_tail(Node(1))
    ll.add_in_tail(Node(2))
    ll.add_in_tail(Node(3))
    ll.add_in_tail(Node(2))
    ll.add_in_tail(Node(4))

    def test_linked_list_1(self):
        self.ll.delete(2, all=False)
        print('Delete', self.ll.read_list())

    def test_linked_list_2(self):
        self.ll.delete(2, all=True)
        print('Delete all', self.ll.read_list())

    def test_linked_list_3(self):
        self.ll.clean()
        print('Clean', self.ll.read_list())

    def test_linked_list_4(self):
        found = self.ll.find_all(1)
        print('Fin 1', len(found))

    def test_linked_list_5(self):
        print('Len', self.ll.len())

    def test_linked_list_6(self):
        llt = LinkedList()
        llt.insert(None, Node(1))
        print('Insert', llt.read_list())

        node1 = llt.find(1)
        llt.insert(node1, Node(2))
        print('Insert 2', llt.read_list())

        llt.insert(None, Node(0))
        print('Insert 3', llt.read_list())

list = TestLL()
list.test_linked_list_1()
list.test_linked_list_2()
list.test_linked_list_3()
list.test_linked_list_4()
list.test_linked_list_5()
list.test_linked_list_6()
