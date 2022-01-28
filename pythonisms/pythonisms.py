from pythonisms.linked_list import LinkedList

#Let's take a basic linked list and make it a bit cooler.

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

    def __eq__(self, other):
        return list(self) == list(other)

    def __str__(self):
        as_string = ""

        for val in self:
            as_string += f"{{ {val} }} -> "

        as_string += "None"
        return as_string

    def __add__(self, other):
        combined_list = list(self) + list(other)
        return CoolerLinkedList(combined_list)