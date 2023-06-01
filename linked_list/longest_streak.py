from create_linked_list import create_linked_list


def longest_streak(head, streak_values=[]):
    """Return the longes consecutive streak of the same value.
    >>> head = create_linked_list(values=[2, 3, 3, 7, 7, 7, 1])
    >>> longest_streak(head)
    3
    >>> longest_streak(head=None)
    0
    >>> longest_streak(head=create_linked_list(values=[11]))
    1
    >>> longest_streak(head, streak_values=[3, 7])
    5
    >>> longest_streak(head=None, streak_values=[1,2,3])
    0
    >>> longest_streak(head=create_linked_list(values=[11]), streak_values=[1,2,3])
    0
    """
    max_streak = 0
    current_streak = 0
    prev_val = None
    curr = head
    while curr is not None:
        if curr.val == prev_val and curr.val in streak_values:
            current_streak += 1
        else:
            current_streak = 0

        if current_streak > max_streak:
            max_streak = current_streak
        
        prev_val = curr.val
        curr = curr.next

    return max_streak
