def count_repeated_chars(s):
    count = 0
    for char in set(s):
        if s.count(char) > 1:
            count += 1
    return count


def test_count_repeated_chars():
    assert count_repeated_chars("hello") == 2
    assert count_repeated_chars("world") == 1
    assert count_repeated_chars("Mississippi") == 4
    assert count_repeated_chars("programming") == 2


test_count_repeated_chars()
