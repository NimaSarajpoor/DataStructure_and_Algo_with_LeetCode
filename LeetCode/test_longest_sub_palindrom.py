from longest_sub_palindrom import longest_sub_palindrom

def test_SingleElement():
    assert longest_sub_palindrom("a") == "a"

def test_AllSame():
    assert longest_sub_palindrom("aaaaa") == "aaaaa"


# def test_AllDifferent():
#    assert longest_sub_palindrom("abcde") == ??
# how to use assert with "or"? because, the output of longest_sub_palindrom("abcde")
# can be any of those letters (logically speaking)

def test_hard_to_find():
    assert longest_sub_palindrom("abccbdddbc") == "cbdddbc"
