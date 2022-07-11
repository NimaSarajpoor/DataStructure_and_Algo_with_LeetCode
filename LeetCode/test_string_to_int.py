from string_to_int import string_to_int

def test_singledigit():
    assert string_to_int("2") == 2
    assert string_to_int("-2") == -2

    assert string_to_int("   +2") == 2
    assert string_to_int("   -2") == -2


def test_complexcase_1():
    assert string_to_int("   -2ABC12.3") == -2


def test_complexcase_2():
    assert string_to_int("   -232ABC") == -232


def test_complexcase_3():
    assert string_to_int("   -ABC242") == 0
