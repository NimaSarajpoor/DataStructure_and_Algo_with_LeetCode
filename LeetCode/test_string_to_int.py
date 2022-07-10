from string_to_int import string_to_int

def test_singledigit():
    assert string_to_int("2") == 2
    assert string_to_int("-2") == -2

    assert string_to_int("   +2") == 2
    assert string_to_int("   -2") == -2


def test_complexcase():
    assert string_to_int("   -2ABC12.3") == -2123
