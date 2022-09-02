
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


# #linked_list --------------------/
# from linked_lists.linked_list_func import Node, LinkedList
 
# linked_list = LinkedList()
# linked_list.head = Node('Olma')
# fruit1 = Node('Olcha')
# fruit2 = Node('Anor')
# fruit3 = Node('Behi')
# fruit4 = Node("shaftoli")
# linked_list.head.next = fruit1
# fruit1.next = fruit2
# fruit2.next = fruit3
# linked_list.push('banana')
# linked_list.insertAfter(fruit1, 'nok')
# linked_list.append('Olxori')
# print(linked_list.print_all_data(), '\n-----------------------------------------')
# linked_list.delete_node('behi')
# # print()
# print(linked_list.print_all_data())

## selfection sort ---------------------
# from selection_sort.selection_sort import SelectionSort

# my_list = [1, 8, 9, 12, 122, 4, 5, 7, 12, 1]
# n_list = []
# n1_list = [2]
# sort = SelectionSort(my_list)
# print(sort.sort_by_decriese())
# print(sort.sort_by_incriese())
# print(sort.sorted_list)


# string_list = ['olma', 'anor', 'behi', 'olcha', 'nok']
# sort_string = SelectionSort(string_list)
# print(sort_string.sort_by_decriese())
# #+-------------- end selection sort --------------------


# + ------- Stack ------------------
from stacks.stack import Stack

my_stack = Stack()
print(my_stack.isEmpty())

my_stack.push('initial_data')
my_stack.push(152)
my_stack.push("fruits")
print(my_stack.peek())

print(my_stack.pop())
print(my_stack.peek())

# ------------------ end stack ---------------