def is_palindrome(s):
    if len(s) < 3:
        raise ValueError("Палиндром должен содержать как минимум 3 символа")

    s = s.replace(" ", "").lower()

    return s == s[::-1]


def test_is_palindrome():
    assert is_palindrome("level") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == False


test_is_palindrome()
