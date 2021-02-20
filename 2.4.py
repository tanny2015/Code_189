from LinkList import LinkedList

def partition(llist, par):
    i = llist.head
    if i is None:
        return
    i_slow = i
    small_head, small_tail, big_head, big_tail = None, None, None, None
    while i is not None:
        if i.data < par:
            if small_head is None:
                small_head = i
                small_tail = i
                # if i_slow != llist.head:
                #     i_slow.next = None
            else:
                small_tail.next = i
                small_tail = i
        else:
            if big_head is None:
                big_head = i
                big_tail = i
            else:
                big_tail.next = i
                big_tail = i
        i_slow = i
        i = i.next
        ## 这一步是最重要的。主要是把一些没用的链接马上砍掉，因为没用的链接容易导致‘环’的出现！
        # i_slow.next = None

    ## 这一步是最重要的。主要是把一些没用的链接马上砍掉，因为没用的链接容易导致‘环’的出现！
    if big_tail is not None:
        big_tail.next = None

    if small_tail is not None:
        if big_head is not None:
            small_tail.next = big_head
        return small_head
    else:
        return big_head

from LinkList import print_from_head_node
llist = LinkedList()
llist.initial_with_string("abcdefghi")  # i-h-g-f-e-d-c-b-a (del = e)
print_from_head_node(partition(llist, 'c'))
