class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f'[{self.data}]->{self.next}'


class LinkedList:
    def __init__(self, object) -> None:
        self.head = object

    def push_back(self, object):

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = object

    def push_front(self, object):

        temp = self.head
        object.next = temp
        self.head = object

    def pop_back(self):
        temp = self.head

        if temp.next is None:
            return None

        while temp.next.next:
            temp = temp.next
        temp.next = None

    def pop_front(self):
        temp = self.head
        self.head = temp.next

    def insert(self, object):
        pass

    def erase(self, object):
        pass

    def length(self):

        temp = self.head
        count = 1
        while temp.next:
            temp = temp.next
            count += 1

        return count

    def __str__(self) -> str:
        return f'{self.head}'


linked_list = list(range(6))

first = Node(1)
lnk_lst = LinkedList(first)

for i in range(2, 5):
    lnk_lst.push_back(Node(i))

lnk_lst.push_front(Node(-1))
print(lnk_lst)
print(lnk_lst.length())

lnk_lst.pop_front()
print(lnk_lst)

lnk_lst.pop_back()
print(lnk_lst)
