from link_list import Node, LinkedList

'''
Напишите функцию, которая получает на вход два связанных списка,
состоящие из целых значений, и если их длины равны,
возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков
'''

def sum_linked_lists(list1, list2):
    result = LinkedList()
    if list1.len() != list2.len():
        return None
    node1 = list1.head
    node2 = list2.head

    while node1 and node2 is not None:
        value_sum = node1.value + node2.value
        result.add_in_tail(Node(value_sum))
        node1 = node1.next
        node2 = node2.next
    return result

list1 = LinkedList()
list1.add_in_tail(Node(4))
list1.add_in_tail(Node(8))
list1.add_in_tail(Node(6))

list2 = LinkedList()
list2.add_in_tail(Node(1))
list2.add_in_tail(Node(7))
list2.add_in_tail(Node(6))

list3 = LinkedList()
list3.add_in_tail(Node(2))
list3.add_in_tail(Node(8))

list4 = LinkedList()
list4.add_in_tail(Node(11))
list4.add_in_tail(Node(22))
list4.add_in_tail(Node(33))

result = sum_linked_lists(list1, list2)
print(result, result.read_list())

result2 = sum_linked_lists(list3, list4)
print(result2)



