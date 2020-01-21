def insertion_sort(lst):
    # At each pass ensure that that section is sorted.
    compares, swapped =0, 0
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        i = todo
        compares += 1
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            i -= 1
            if i != 0:
                compares += 1
            swapped += 1
            
    return compares, swapped