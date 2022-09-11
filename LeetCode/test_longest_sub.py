from longest_sub import len_longest_substr


def test_all_same():
    s = "aaaaaa"
    assert len_longest_substr(s) == 1


def test_single_letter():
    s = "a"
    assert len_longest_substr(s) == 1


def test_all_different():
    s = "abcde"
    assert len_longest_substr(s) == 5


def test_osillation():
    s = "abcabcabc"
    assert len_longest_substr(s) == 3


def test_empty_string():
    s = ""
    assert len_longest_substr(s) == 0


def test_last_same_as_first():
    s = "abcda"
    assert len_longest_substr(s) == 4


def test_has_repeats():
    s = "abcdccfghijkf"
    assert len_longest_substr(s) == 7


def test_long_s():
    s = "abcdefghi" * 1000
    assert len_longest_substr(s) == 9
