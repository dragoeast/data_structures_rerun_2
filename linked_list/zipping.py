from create_linked_list import create_linked_list
from node import Node


def zipping_linked_lists(*head_lst):
    """Return a list of 
    >>> head_1 = create_linked_list(values=[ ch for ch in "abcd" ]))
    >>> head_2 = create_linked_list(values=[ ch for ch in "pqr" ]))
    >>> head_3 = create_linked_list(values=[ ch for ch in "xyz" ]))
    >>> zipping_linked_lists(*head_lst=*[head_1, head_2, head_3])
    [ (ch1, ch2, ch3) for ch1, ch2, ch3 in zip(["abc", "pqr", "xyz"]) ]
    """
    counter = 0
    curr_lst = head_lst[:]
    size = len(curr_lst)
    first_head = curr_lst[0]
    tail = first_head
    

    while all([curr is not None for curr in curr_lst]):
        for index in range(1, size+1):
            curr_index = index % size
            curr = curr_lst[curr_index]
            tail.next = curr
            curr = curr.next
            tail = tail.next
        
        curr_lst = [curr.next for curr in curr_lst]

    for curr in curr_lst:
        if curr is not None:
            _curr = curr
            while _curr is not None:
                tail.next = _curr
                tail = tail.next
                _curr = _curr.next
            

    return first_head

head_1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
head_2 = Node(10, Node(11, Node(12)))
head_3 = Node(100, Node(101, Node(102)))
print(zipping_linked_lists(*[head_1, head_2, head_3]))
