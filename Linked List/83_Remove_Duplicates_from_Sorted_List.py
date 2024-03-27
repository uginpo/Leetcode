from typing import Optional


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f'[{self.data}]->{self.next}'


class LinkedList:
    def __init__(self):
        self.head = None

    def lenght(self):
        count = 0
        temp = self.head

        while self.head:
            temp = temp.next
            count += 1

        return count

    def __str__(self) -> str:
        return str(self.head)


head1 = [1, 1, 2, 3, 3]

linkes_list = LinkedList()
temp = Node(head1[0])
linkes_list.head = temp

for i in range(1, len(head1)):
    temp.next = Node(head1[i])
    temp = temp.next


print(linkes_list)
print(linkes_list.lenght())
