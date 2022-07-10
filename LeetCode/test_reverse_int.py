from reverse_int import reverse_int

def test_positive_SingleDigit():
    assert reverse_int(8) == 8

def test_positive():
    num = 1829723
    assert reverse_int(num) == int(str(num)[::-1])

def test_positive_max():
    num = 2147483647
    num = int(str(num)[::-1])
    assert reverse_int(num) == int(str(num)[::-1])

def test_positive_max_exceeded():
    num = 2147483648
    num = int(str(num)[::-1])
    assert reverse_int(num) == 0

def test_negative_SingleDigit():
    assert reverse_int(-7) == -7

def test_negative():
    num = -1829723
    assert reverse_int(num) == -1 * int(str(abs(num))[::-1])

def test_negative_max():
    num = -2147483648
    num = -1 * int(str(abs(num))[::-1])
    assert reverse_int(num) == -1 * int(str(abs(num))[::-1])

def test_negative_max_exceeded():
    num = -2147483649
    num = -1 * int(str(abs(num))[::-1])
    assert reverse_int(num) == 0
