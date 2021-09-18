def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    
    frequency = {}

    for val in nums:
        frequency[val] = frequency.get(val, 0) + 1

    most_frequent = max(frequency.values())

    modes = [key for key, val in frequency.items() if val == most_frequent]

    return val
  



    
    

