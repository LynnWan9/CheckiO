def split_pairs(a):
    # create a new empty list to store pairs
    list_after_split = []
    # if the string contains an odd number of characters
    # append an underscore to the string
    if len(a) % 2 != 0: 
        a += '_'
    # store pairs in the new list
    for i in range(0, len(a), 2):
        list_after_split.append(a[i:i+2])
    # return the new list
    return list_after_split


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
