class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_all_data(self):
        temporary = self.head
        while temporary:
            print(temporary.data)
            temporary = temporary.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print('Prev node is not defined')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next 
        prev_node.next = new_node


    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data.lower().__contains__(key.lower()):
            self.head =  temp.next
            temp = None
            return

        while temp:
            if temp.data.lower().__contains__(key.lower()):
                break
            prev = temp
            temp = temp.next
        if temp is None:
            print('data is not inside of the list')
            return
        prev.next = temp.next
        temp = None