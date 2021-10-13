def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    if stop < start: 
        return "stop input must be greater than start input"
    else:
        count = start
        while count <= stop: 
            print (count)
            count += 1
    return ""


print (count_up(5, 7))
