from sort import DoubleLinkList

class Stack:
    def __init__(self):
        self.__list = DoubleLinkList()

    def push(self, vals):
        self.__list.add(vals)
    
    def pop(self):
        if self.__list.size == 0:
            return print("Array Empty")
        else:
            val = self.__list.last()
            self.__list.remove_last()
            return print(val)

    def peek(self):
        return self.__list.last()

    def isEmpty(self):
        return self.__list.size == 0
    
    def __len__(self):
        return self.__list.size


# my_stack = Stack()

# my_stack.push(10)
# my_stack.push(20)
# my_stack.push(30)
# my_stack.push(40)

# print(my_stack.peek())
# print(len(my_stack))
# my_stack.pop()
# print(len(my_stack))

class Queue:
    def __init__(self):
        self.__quee = DoubleLinkList()

    def enqueue(self, value):
        self.__quee.add(value)

    def dequee(self):
        val = self.__quee.fast()
        self.__quee.Remov_first()
        return val
    
    def first(self):
        self.__quee.fast()
    
    def isEmpty2(self):
        return self.__quee.size == 0

    def __len__(self):
        return self.__quee.size

