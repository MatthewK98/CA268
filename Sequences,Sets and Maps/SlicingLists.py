import sys
line = sys.stdin
def get_sliced_lists(lst):
    no_last = lst[:-1]
    no_first_or_last = lst[1:-1]
    reverse = lst[::-1]
    return [no_last,no_first_or_last,reverse]