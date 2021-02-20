

from LinkList import LinkedList
# head is the head of the linklist
# if they dont give you any limitation in the linklist, I think double linkedlist is better to use
# but need to explain to your interviewer! if using singly linklist,
# you may need one more pointer to get the prev node of the current node! Not Necessary to do that trivial.

def remove_duplicate(linklist): #O(N)
    head = linklist.head
    d = dict()
    if head is None:
        return

    it = head
    d[it.data] = 1

    while it.next:
        if it.next.data in d:
            # remove duplicate
            it.next = it.next.next
            continue # ***important
        else:
            d[it.next.data] = 1
            if it.next:
                it = it.next
            else:
                break

    linklist.print()


# linkL = LinkedList()
# linkL.initial_with_string("fdsgfafffff")
# # f-f-f-f-f-a-f-g-s-d-f
# remove_duplicate(linkL)
# # result: f a g s d # 注意insert的order是从head插入的，因此顺序是相反的

from Doubly_LinkList import DoublyLinkedList
# I decide to use doubly linked list.
def remove_duplicate_no_buffer(doubly_linklist):
    head = doubly_linklist.head
    it1, it2 = head, head

    while it1 is not None :
        it2 = it1.next
        while it2 is not None:
            if it2.data == it1.data:
                doubly_linklist.deleteNode(it2)
            it2 = it2.next
        it1 = it1.next
    # the head node will never be deleted, so you can do it without considering moving the head pointer
    doubly_linklist.printList(head)


linkL = DoublyLinkedList()
linkL.initial_with_string("fdsgfafffff")
# f-f-f-f-f-a-f-g-s-d-f
remove_duplicate_no_buffer(linkL)
# result: f d s g a