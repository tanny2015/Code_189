# from https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
# from Node import Node  # **Dont directly import Node(if the file names 'Node.py', it will report Node is not callable


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print(self):
        it = self.head
        while it:
            print(it.data, end=' ')
            it = it.next
        print('\n')

    def initial_with_string(self, string_name):
        if (len(string_name) == 0 or string_name == None):
            print("ERROR! string can not be empty \n")
            return

        # Iterate over the string
        for element in string_name:
            # print(element, end=' ')
            self.insert(element)

    def initial_with_list(self, l):
        if len(l) == 0 or l == None:
            print("ERROR! list can not be empty \n")
            return

        # Iterate over the string
        for element in l:
            # print(element, end=' ')
            self.insert(element)

        # self.print()

def print_from_head_node(head):
    it = head
    while it:
        print(it.data, end=' ')
        it = it.next
    print('\n')

# hd = Node('a', None)
# list1 = LinkedList(hd)
# print(list1.head.data)

# lt = LinkedList()
# lt.initial_with_string('abcdedf')
