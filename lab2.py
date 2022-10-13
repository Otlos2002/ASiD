from typing import Any

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    value: Any
    next: 'Node'

    def getNext(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    head: Node
    tail: Node
    def __str__(self):
        tekst = ''
        wsk = self.head
        while True:
            if wsk.next is None:
                tekst += f'{wsk.value}'
                return tekst
            tekst += f'{wsk.value} -> '


    def push(self, new_data):

        # 1 & 2: Allocate the Node &
        #     Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    def append(self, item):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))
        else:
            self.head = Node(item)







    def length(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        return count



llist = LinkedList()
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(21)
llist.push(14)
llist.push(1453)

print("Count of nodes is :", llist.length())
print(llist)










