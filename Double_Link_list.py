class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.data = value


class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tall = None
        self.size = 0


    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tall = node
            self.size += 1

        else:
            self.tall.next = node
            node.prev = self.tall
            self.tall = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        
        if node.next is None:
            self.tall = node.prev
        else:
            node.next.prev = node.prev


    def remove(self, val):
        node = self.head

        while node is not None:
            if node.data == val:
                self.__remove_node(node)
            node = node.next

    def __insert_node(self,nod, dirictionVal, node):
        insert = Node(node)
        
        if nod.prev is None :
           insert.next = self.head
           insert.prev = None

           # if self.head is not None:
           self.head.prev = insert

           self.head = insert
        else:
            insert.next = dirictionVal.next
            dirictionVal.next = insert
            insert.prev = dirictionVal


            if insert.next is not None:
                insert.next.prev = insert

            

        
            
            
        


    def insert_after(self, nextVal, node):
        nod = self.head
        while nod is not None:
            if nod.data == nextVal:
                self.__insert_node(nod,nod, node)
            nod = nod.next

    def __str__(self):
        node = self.head
        vals = []
        while node is not None:
            vals.append(node.data)
            node = node.next
        return f"[{', '.join(str(data) for data in vals)}]"


my_list = DoubleLinkList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
print(my_list)

print(my_list)

my_list.insert_after(1, 5)
print(my_list)
