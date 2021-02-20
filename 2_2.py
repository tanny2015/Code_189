import LinkList
from LinkList import LinkedList

# !!!! 这个答案是错误的！ 不是题目要求的！
def re_kth_to_end(llist_head, kth):
    if llist_head is None:
        return None

    i = 1
    it = llist_head
    while it is not None:
        if i != kth:
            i += 1
            it = it.next
        else:
            # return new linked list
            LinkList.print_from_head_node(it)
            return it

    # kth is larger than the size of the total nodes
    # return null
    return None

# llist = LinkedList()
# llist.initial_with_string("abcdefg")  # g-f-e-d-c-b-a
# LinkList.print_from_head_node(re_kth_to_end(llist.head, 3))

# space O(n)
def printKthToLast(head, k):
    if head is None:
        return 0

    index = printKthToLast(head.next, k) + 1
    if index == k:
        print(k, "th to last node is ", head.data)

    return index

# llist = LinkedList()
# llist.initial_with_string("abcdefg")  # g-f-e-d-c-b-a
# printKthToLast(llist.head, 3)

# Space O(1)  time O(n)
def returnKthToLast(head, k):
    fast = head
    # for _ in range(1, k): #range(10) is 0~9 range(1,3) = [1,2]
    #   if fast:
    #       fast = fast.next
    #   else:
    #       return None

    # let fast pointer go k step in advance
    i = 1
    while i <= k:
        if fast:
            fast = fast.next
            i += 1
        else:
            return None


    slow = head
    # fast is now k nodes ahead of slow

    while fast:
        fast = fast.next
        slow = slow.next

    return slow


llist = LinkedList()
llist.initial_with_string("abcdefg")  # g-f-e-d-c-b-a
LinkList.print_from_head_node(returnKthToLast(llist.head, 3))
