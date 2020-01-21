def make_adjacency_matrix(edge_list):
    """ this function create an adjacency matrix representation of a graph using the supplied edge list
    """
    # Maybe start with an empty adjacency matrix
    adjacency_matrix = []
    vals = []
    for relations in edge_list:
        for val in relations:
            if val not in vals:
                vals.append(val)
            
    vals.sort()
    val = "".join(vals)
    for relations in edge_list:
        a = []
        for i in range(len(vals)):
            if vals[i] in relations:
                a.append(1)
                
            else:
                a.append(0)
        adjacency_matrix.append(a)
    
    # Insert code here
    
    return adjacency_matrix