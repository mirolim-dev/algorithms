
# # task1 by linear search
# from linear_search.task1 import LinearSearch
# print(LinearSearch(list=list).search(127))
# # ----------------------------------

# # # task1 by binary_search ----- 

# from binary_search.task1 import BinarySearch
# list = [x for x in range(1, 10240)]
# # print(list)
# print(BinarySearch(list).search(120))
# # --------------------------------


# linked_list --------------------
from linked_lists.linked_list_func import Node, LinkedList

linked_list = LinkedList()
linked_list.head = Node('Olma')
fruit1 = Node('Olcha')
fruit2 = Node('Anor')
fruit3 = Node('Behi')
fruit4 = Node("shaftoli")
linked_list.head.next = fruit1
fruit1.next = fruit2
fruit2.next = fruit3
linked_list.push('banana')
linked_list.insertAfter(fruit1, 'nok')
linked_list.append('Olxori')
print(linked_list.print_all_data(), '\n-----------------------------------------')
linked_list.delete_node('behi')
# print()
print(linked_list.print_all_data())

