# def inserSort(parameter):

#     for i in range(1, len(parameter)):

#         key = parameter[i]

#         j = i -1
#         while j >= 0 and key < parameter[j]:
#             parameter[j + 1] = parameter[j]
#             j = j - 1
#         parameter[j + 1] = key
# arr = [99, 2, 44, 5, 64, 33, 23, 55]
# inserSort(arr)
# for i in range( len(arr)):
#     print('arr =', arr[i])

#------------------------------------------------
class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.val = value

class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tall = None
        self.size = 0


    def add(self, val):
        node = Node(val)
        if self.tall is None:
            self.head = node
            self.tall = node
            self.size += 1
        else:
            self.tall.next = node
            node.prev = self.tall
            self.tall = node
            self.size += 1
    def _remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tall = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1

    def remove(self, value):
         node = self.head
         while node is not None:
            if node.val == value:
                self._remove_node(node)
                break
            node = node.next

    def remove_last(self):
        if self.tall is not None:
            self._remove_node(self.tall)

    def Remov_first(self):
        if self.head is not None:
            self._remove_node(self.head)

    def fast(self):
        return self.head.val

    def last(self):
        return self.tall.val

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"

    
        

