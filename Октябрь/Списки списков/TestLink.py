from link_list import Node, LinkedList




def test_linked_list_1():
    lst = LinkedList()
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(3))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(4))

    lst.delete(2, all=False)
    print('Delet', lst.to_list())

def test_linked_list_2():
    lst = LinkedList()
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(3))
    lst.add_in_tail(Node(2))

    lst.delete(2, all=True)
    print('Delet all', lst.to_list())

def test_linked_list_3():
    lst = LinkedList()
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(3))

    lst.clean()
    print('Clean', lst.to_list())

def test_linked_list_4():
    lst = LinkedList()
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(3))
    lst.add_in_tail(Node(1))

    found = lst.find_all(1)
    print('Fin 1', len(found))

def test_linked_list_5():
    lst = LinkedList()
    lst.add_in_tail(Node(1))
    lst.add_in_tail(Node(2))
    lst.add_in_tail(Node(3))
    print('Len', lst.len())

def test_linked_list_6():
    lst = LinkedList()
    lst.insert(None, Node(1))
    print('Insert', lst.to_list())

    node1 = lst.find(1)
    lst.insert(node1, Node(2))
    print('Insert 2', lst.to_list())

    lst.insert(None, Node(0))
    print('Insert 3', lst.to_list())

test_linked_list_1()
test_linked_list_2()
test_linked_list_3()
test_linked_list_4()
test_linked_list_5()
test_linked_list_6()
