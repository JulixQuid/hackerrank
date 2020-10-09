# Arrays

def hourglassSum(arr):
    """
        Function that calculates the max hourglass sum from an 6x6 array
    Args:
        arr: 6x6 array

    Returns:
        maximum hourglass sum
    """
    max_value = arr[0][0]+arr[0][1]+arr[0][2]\
                     +arr[1][1]\
           +arr[2][0]+arr[2][1]+arr[2][2]
    for i in range(4):
        for j in range(4):
            ref_hg_value = arr[0+i][0+j]+arr[0+i][1+j]+arr[0+i][2+j]\
                                        +arr[1+i][1+j]\
                          +arr[2+i][0+j]+arr[2+i][1+j]+arr[2+i][2+j]
            if ref_hg_value>max_value:
                max_value = ref_hg_value
    return max_value


def arrayManipulation_fail1(n, queries):
    #failed in half of the cases for time
    # time complexity o(n2)
    borders = set()
    for query in queries:
        borders.add(query[0])
        borders.add(query[1])
    borders = list(borders)
    i_t = {borders[i]: i for i in range(len(borders))}
    values = [0]*len(borders)
    for query in queries:
        for i in range(i_t[query[0]],i_t[query[1]]+1):
            values[i] = values[i]+query[2]
    return max(values)

def arrayManipulation_fail2(n, queries):
    #failed in half of the cases for time
    # time complexity o(n2)
    ref = 0
    for query in queries:
        ref_0 = 0
        ref_1 = 0
        for query_i in queries:
            if query[0] in range(query_i[0],query_i[1]+1):
                ref_0 = ref_0 + query_i[2]
            if query[1] in range(query_i[0], query_i[1]+1):
                ref_1 = ref_1 + query_i[2]
        ref=max(ref,ref_0,ref_1)
    return ref


def arrayManipulation(n, queries):
    """
        Founds the maximum value after applying the queries
    Args:
        n: size  of the array
        queries: queries to execute

    Returns:
        maximum value
    """
    borders = set()
    for query in queries:
        borders.add(query[0])
        borders.add(query[1])
    borders = sorted(borders)
    values = [0]*(len(borders)+1)
    i_t = {borders[i]: i for i in range(len(borders))}
    for query in queries:
        values[i_t[query[0]]] = values[i_t[query[0]]] + query[2]
        values[i_t[query[1]]+1] = values[i_t[query[1]]+1] - query[2]
    ref = 0
    max_ref = 0
    for i in values:
        ref += i
        max_ref = max(ref, max_ref)
    return max_ref



