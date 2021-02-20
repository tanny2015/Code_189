from LinkList import LinkedList
# import math

def sum_list_reverse(llist1, llist2):
    value1, value2 = 0, 0
    if llist1.head is None:
        value1 = 0
    if llist2.head is None:
        value2 = 0

    it1 = llist1.head
    it2 = llist2.head
    i1 = 0
    i2 = 0
    while it1 is not None:
        value1 += it1.data * pow(10, i1)
        it1 = it1.next
        i1 += 1

    while it2 is not None:
        value2 += it2.data * pow(10, i2)
        it2 = it2.next
        i2 += 1

    total_sum = value1 + value2
    print(value1, value2)

    llist = LinkedList()

    # 以下这步必须先做
    # llist.insert(total_sum % 10)
    digits_reverse_store(llist, total_sum)
    llist.print()


def digits_reverse_store(llist, digit):
    if digit <= 0:
        return

    digits_reverse_store(llist, digit // 10)
    llist.insert(digit % 10)


# l1 = LinkedList()
# l1.initial_with_list((6, 1, 7))
# l2 = LinkedList()
# l2.initial_with_list((2, 9, 5))
# sum_list_reverse(l1, l2)





######################## follow up
def sum_follow_up(t1, t2, llist):
    if t1 is None and t2 is None:
        return

    value1, value2 = 0, 0
    if t1 is not None:
        value1 = t1.data
        t1 = t1.next

    if t2 is not None:
        value2 = t2.data
        t2 = t2.next

    sum_follow_up(t1, t2, llist)
    possible_decimal = 0
    if llist.head is not None:
        possible_decimal = llist.head.data // 10
        if possible_decimal > 0:
            llist.head.data = llist.head.data % 10

    digit = (value1 + value2) + possible_decimal
    llist.insert(digit) # 注意，此时该节点变成 head node 了

def sol_follow_up(llist1, llist2):
    llist = LinkedList()
    sum_follow_up(llist1.head,llist2.head,llist)

    # 这个方法的瑕疵在于，这一步的操作其实应该是递归方程里边重复的一个部分，但是由于最后一步没法并入递归，所以只能在
    # 外边另外写一遍了
    possible_decimal = 0
    if llist.head is not None:
        possible_decimal = llist.head.data // 10
        if possible_decimal > 0:
            llist.head.data = llist.head.data % 10
            llist.insert(possible_decimal)

     # 注意，此时该节点变成 head node 了
    llist.print()


l1 = LinkedList()
l1.initial_with_list((7, 1, 6))
l2 = LinkedList()
l2.initial_with_list((5, 9, 2))
l1.print()
l2.print()
sol_follow_up(l1, l2)

