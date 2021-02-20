# 一个stack（full_multi_stack) 里边包含3个小的stack
class small_stack:
    def __init__(self, bottom_box_index, capacity):
        self.bottom_box_index = bottom_box_index
        self.capacity = capacity
        self.top_index = self.bottom_box_index - 1  # meaning: empty
        self.size = 0
        # self.stack_id = stack_id  # to identity which stack it is (there are totally 3 stacks)

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def push(self, data, array):
        # the stack items are growing to the left side  newitem<-olderitem<-even_olderitem-...
        if not self.is_full():
            self.top_index -= 1  # new index is located in the left
            array[self.top_index] = data
            self.size += 1
        else:
            print("Warning: stack is full! push failed \n")
            return

    def pop(self, array):
        if self.is_empty():
            print("Warning: stack is empty! pop failed \n")
            return
        else:
            temp = array[self.top_index]
            # left it alone to let the later data overwriting this slot
            # array[self.top_index] = None # not sure if that is a digit or a pointer, so not do this
            self.top_index -= 1
            self.size -= 1
            return temp

    def peek(self, array):
        if self.is_empty():
            print("Warning: stack is empty! peek failed \n")
            return None
        else:
            return array[self.top_index]


# stack1 = small_stack(1, 2)


# 一个stack（full_multi_stack) 里边包含3个小的stack
class full_multi_stack:
    def __init__(self, num_of_stack, array):
        i = 0
        while (i < num_of_stack):
            capacity = len(array) // num_of_stack
            bottom_box_index = capacity * (i + 1) - 1
            stack = small_stack(bottom_box_index, capacity)
            array.append(stack)

    # 小stack的数量
    num_of_stack = 3

    def __int__(self, ):
        num_of_stack
