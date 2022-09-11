from longest_sub_palindrom import naive_longest_sub_palindrom
from longest_sub_palindrom import naive_longest_sub_palindrom_enhanced


def test_SingleElement():
    assert naive_longest_sub_palindrom("a") == "a"
    assert naive_longest_sub_palindrom_enhanced("a") == "a"


def test_AllSame_Odd():
    assert naive_longest_sub_palindrom("aaaaa") == "aaaaa"
    assert naive_longest_sub_palindrom_enhanced("aaaaa") == "aaaaa"


def test_AllSame_Even():
    assert naive_longest_sub_palindrom("aaaa") == "aaaa"
    assert naive_longest_sub_palindrom_enhanced("aaaa") == "aaaa"


# def test_AllDifferent():
#    assert longest_sub_palindrom("abcde") == ??
# how to use assert with "or"? because, the output of longest_sub_palindrom("abcde")
# can be any of those letters (logically speaking)


def test_hard_to_find():
    assert naive_longest_sub_palindrom("abccbdddbc") == "cbdddbc"
    assert naive_longest_sub_palindrom_enhanced("abccbdddbc") == "cbdddbc"
