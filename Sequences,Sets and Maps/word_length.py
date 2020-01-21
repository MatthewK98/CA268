def get_counts_dict(lst):
    len_dict = {}
    for word in lst:
        if len(word) not in len_dict:
            len_dict[len(word)] = 1
        else:
            len_dict[len(word)] += 1
    return len_dict