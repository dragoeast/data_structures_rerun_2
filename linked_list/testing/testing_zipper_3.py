from ..node import Node
from create_linked_list import create_linked_list
from zipper import zipper_3
from values import get_values

def testing():
    head_1 = create_linked_list(values=[ value for value in "abc" ])
    head_2 = create_linked_list(values=[ value for value in "pqr" ])
    head_3 = create_linked_list(values=[ value for value in "xyz" ])
    zipped_head_3 = zipper_3(head_1, head_2, head_3)
    result = ['a', 'p', 'x', 'b', 'q', 'y', 'c', 'r', 'z']
    assert get_values(head=zipped_head_3) == result, f"should be {result}"

if __name__ == "__main__":
    testing()
    print("Everything passed")
