def sum_to_k(lst, k):
    i = 0
    j = len(lst) - 1
    l = 0
    while i < len(lst): 
        if len(lst) % 2 != 0 and j == l:
            pass


        else:
            total = lst[l] + lst[j]
            if total < k:
                l += 1

            elif total > k:
                j -= 1
            if total == k:
                return True
        i += 1

    return False