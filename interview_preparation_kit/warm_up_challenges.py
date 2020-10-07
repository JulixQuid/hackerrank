# warm up challenges


def countingValleys(steps, path):
    """
        function that counts the valleys from the path
    Args:
        steps: int
             the number of steps on the hike
        path: string
            a string describing the path

    Returns:
        valleys: int
            number of valleys in the path
    """
    i = 0
    previous = 0
    altitude = 0
    valleys = 0

    for i in range(steps):

        previous = altitude
        if path[i] == 'D':
            altitude -= 1
        if path[i] == 'U':
            altitude += 1
        if altitude == 0 and previous < 0:
            valleys += 1
        print(altitude)
    return valleys







def sockMerchant(n, ar):
    """
        It must return an integer representing the number of matching pairs of
        socks that are available.

    Args:
        n: int
            the number of socks in the pile
        ar: list
            the colors of each sock

    Returns:
        pairs: int
            the number of matching pairs
    """
    pair_control = dict()
    for sock in ar:
        if sock in pair_control.keys():
            pair_control[sock] += 0.5
        else:
            pair_control[sock] = 0.5
    pairs = sum([int(total) for total in pair_control.values()])
    return pairs
