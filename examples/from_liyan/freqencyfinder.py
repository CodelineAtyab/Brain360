def counter(input_list):
    """
    This function takes a list and counts the frequency of each element.
    """
    freq = {}
    for i in input_list:
        freq[i] = freq.get(i, 0) + 1
        print(i, freq[i])
    return freq

print(counter([1, 2, 3, 4, 5, 5, 5, 2, 2, 2, 2, 3]))