from pythonisms.pythonisms import CoolerLinkedList as LinkedList


def test_linked_list_init():
    li = [1, 2, 3]
    example = LinkedList(li)
    assert str(example) == '{ 1 } -> { 2 } -> { 3 } -> None'


def test_linked_list_cast_list():
    li = [1, 2, 3]
    example = LinkedList(li)
    assert list(example) == [1, 2, 3]


def test_linked_list_comprehension():
    li = [1, 2, 3]
    example = LinkedList(li)
    assert [num**2 for num in example] == [1, 4, 9]


def test_eq_comparison():
    ll_1 = LinkedList([1, 2, 3])
    ll_2 = LinkedList([1, 2, 3])

    assert ll_1 == ll_2


def test_eq_comparison_not_same():
    ll_1 = LinkedList([1, 2, 3])
    ll_2 = LinkedList([3, 2, 1])

    assert ll_1 != ll_2


def test_dunder_add():
    ll_1 = LinkedList([1, 2, 3])
    ll_2 = LinkedList([3, 2, 1])

    ll_3 = ll_1 + ll_2

    assert list(ll_3) == [1, 2, 3, 3, 2, 1]
    assert list(ll_1) == [1, 2, 3]
    assert list(ll_2) == [3, 2, 1]


def test_cast_set():
    li = [1, 2, 3]
    example = LinkedList(li)
    assert set(example) == {1, 2, 3}


def test_cast_set_duplicates():
    li = [1, 2, 2, 3, 3]
    example = LinkedList(li)
    assert set(example) == {1, 2, 3}
