def make_edge_list(adjacency):
    """ this function create an edge list representation of a graph using the supplied adjacency matrix
    """
    # Maybe start with an empty edge_list
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    edge_list = []
    
    for relation in adjacency:
        a =[]
        for i, value in enumerate(relation, 0):
            if value == 1:
                a.append(alphabet[i])
        edge_list.append(a)
    # Insert code here
    
    return edge_list