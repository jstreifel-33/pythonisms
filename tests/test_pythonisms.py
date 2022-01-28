from pythonisms.pythonisms import CoolerLinkedList as LinkedList


def test_linked_list_init():
    li = [1, 2, 3]
    example = LinkedList(li)
    assert str(example) == '{ 1 } -> { 2 } -> { 3 } -> None'


def test_linked_list_cast_list():
    li = [1, 2, 3]
    example = LinkedList(li)
    assert list(example) == [1, 2, 3]


def test_eq_comparison():
    ll_1 = LinkedList([1, 2, 3])
    ll_2 = LinkedList([1, 2, 3])

    assert ll_1 == ll_2


def test_eq_comparison():
    ll_1 = LinkedList([1, 2, 3])
    ll_2 = LinkedList([3, 2, 1])

    assert ll_1 != ll_2