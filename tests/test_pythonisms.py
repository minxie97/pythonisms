from typing import Any
from pythonisms.pythonisms import LinkedList
from pythonisms.wrappers import addition, say

def test_linked_list_init():
    li = [1, 2, 3]
    test = LinkedList(li)
    assert str(test) == '[ 1 ] -> [ 2 ] -> [ 3 ] -> None'

def test_linked_list_list():
    li = [1, 2, 3]
    test = LinkedList(li)
    assert list(test) == [1, 2, 3]

def test_linked_list_comp():
    li = [1, 2, 3]
    test = LinkedList(li)
    assert [num**3 for num in test] == [1, 8, 27]

def test_linked_list_eq():
    ll1 = LinkedList([1, 2, 3])
    ll2 = LinkedList([4, 5, 6])
    ll3 = LinkedList([1, 2, 3])
    assert ll1 != ll2
    assert ll1 == ll3

def test_linked_list_add():
    ll1 = LinkedList([1, 2, 3])
    ll2 = LinkedList([4, 5, 6])

    assert list(ll1 + ll2) == [1, 2, 3, 4, 5, 6]

def test_intro_outro():
    assert say("hello") == "Drum roll please... hello... Tada!"

def test_timing():
    assert addition(1, 2)