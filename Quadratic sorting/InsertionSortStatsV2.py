def insertion_sort(lst):
    compares, moves =0, 0
    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        i = todo
        compares += 1
        moves += 1
        while i > 0 and tobeinserted < lst[i-1]:
            lst[i] = lst[i-1] # Make space for the item
            i -= 1
            if i != 0:
                compares += 1
            moves += 1
        lst[i] = tobeinserted  # Found the place for this item, plonk it in
        moves += 1
    return compares, moves