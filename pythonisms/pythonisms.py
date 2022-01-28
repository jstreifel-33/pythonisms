from pythonisms.linked_list import LinkedList

#Let's take a basic linked list and make it.... less basic.

class CoolerLinkedList(LinkedList):
    def __init__(self, collection=None):
        super().__init__()
        if collection:
            for val in collection[::-1]:
                self.insert(val)

    def __iter__(self):
        current = self.head

        while current:
            yield current.value
            current = current.next
