from pythonisms.pythonisms import CoolerLinkedList as LinkedList


def test_linked_list_init():
    li = [1, 2, 3]
    example = LinkedList(li)
    assert str(example) == '{ 1 } -> { 2 } -> { 3 } -> None'


def test_linked_list_cast_list():
    li = [1, 2, 3]
    example = LinkedList(li)
    assert list(example) == [1, 2, 3]