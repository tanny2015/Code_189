# Delete Middle Node
# Cracking the Coding Interview (CTCI) 2.3
#
# Question
# You're given a pointer to a node in a singly linked list.
# The node will NOT be the last node in the singly linked list.
# Write a function that deletes only that node in the linked list in-place.
# You don't have to return anything since the deletion is in-place.
#
# 1Linked List - 1 -> 2 -> 3 -> 4 -> 5 -> 3
# 2Input - 4 -> 5 -> 3
# 3Result after running function - 1 -> 2-> 3 -> 5 -> 3

from LinkList import LinkedList
import gc
def delete_mid_node(llist, del_node):
    # according to the question, del_node.pre and del_node.next can not be None
    while del_node.next is not None:
        del_node.data = del_node.next.data
        if del_node.next.next is None:
            break
        else:
            del_node = del_node.next

    # delete the last node
    del_node.next = None
    gc.collect()

llist = LinkedList()
llist.initial_with_string("abcdefghi")  # i-h-g-f-e-d-c-b-a (del = e)
node = llist.head.next.next.next.next
delete_mid_node(llist, node)
llist.print()

