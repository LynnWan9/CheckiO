## string.find(value, start, end) finds the first occurrence of the specified value from 'start' to 'end'.

def second_index(text: str, symbol: str) -> [int, None]:
    if text.count(symbol) < 2: # if the character does not occur at least twice in the text
        return None # return None
    first_index = text.find(symbol) # find the index of the first character occurrence
    return text.find(symbol, first_index + 1) # search from first_index + 1 to get the index of the second character occurrence


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
