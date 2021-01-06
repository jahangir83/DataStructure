class Mnode:
    def __init__(self,data):
        self.Next = None
        self.value = data


class SlinkList:
    def __init__(self):
        self.head = None
        self.tall = None
        self.size = 0

    #Add method create
    def add(self, data):
        node = Mnode(data)

        if self.head is None:
            self.head = node
            self.tall = node
            self.size += 1
        else:
            self.tall.Next = node
            self.tall = node
            self.size +=1

        
    #remove method create
    def removeItem(self, data):
        current = self.head
        prev = self.head

        while current:
            if current.value == data:
                if current == self.head:
                    self.head = current.Next
                else:
                    prev.Next = current.Next
                self.size -= 1
                return
            prev = current
            current = current.Next



    #show item create method
    def printList(self):
        node = self.head
        val = []
        while node is not None:
            val.append(node.value)
            node = node.Next
        print(val)

my_list = SlinkList()

my_list.add("one")
my_list.add(2)

my_list.add(9)
my_list.removeItem("one")
my_list.printList()