# Pythonisms

For this lab I took my basic linked list implementation and added some additional functionality.

* `CoolerLinkedList()` can be passed a collection on instantiation to populate the linked list with values immediately.
* `__iter__` allows for the linked list to be iterated over, as well as casted to various types of collections.
* `__eq__` allows for checking to see if two linked lists contain the same values, in the same order.
* `__add__` allows for the adding together of two linked lists. This enables the concatenation of two linked lists, similar to the python concatenation of normal lists.

`__str__` has also been refactored to use iteration, thanks to the implementation of `__iter__` dunder method.