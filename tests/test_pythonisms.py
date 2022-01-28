from pythonisms.pythonisms import CoolerLinkedList as LinkedList


def test_iter_list_cast():
    li = [1, 2, 3]
    example = LinkedList(li)
    assert str(example) == '{ 1 } -> { 2 } -> { 3 } -> None'