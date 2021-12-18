class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Shopping list is empty")
            return
        item = self.head
        list = ''
        while item:
            list += str(item.data)+' & ' if item.next else str(item.data)
            item = item.next
        print(list)

    def get_length(self):
        count = 0
        item = self.head
        while item:
            count+=1
            item = item.next

        return count

    def insert_head(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_tail(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        item = self.head

        while item.next:
            item = item.next

        item.next = Node(data, None)

    def insert_new(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Error")

        if index==0:
            self.insert_head(data)
            return

        count = 0
        item = self.head
        while item:
            if count == index - 1:
                node = Node(data, item.next)
                item.next = node
                break

            item = item.next
            count += 1

    def remove(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Error")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        item = self.head
        while item:
            if count == index - 1:
                item.next = item.next.next
                break

            item = item.next
            count+=1

    def insert_items(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_tail(data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_items(["Bananas","Eggs","Legos","Shampoo"])
    ll.insert_new(0,"Milk")
    ll.remove(1)
    ll.remove(2)
    ll.insert_new(2,"Water")
    ll.remove(3)
    ll.insert_new(3,"Bread")
    ll.print()
    ll.insert_tail("Xbox")
    ll.print()