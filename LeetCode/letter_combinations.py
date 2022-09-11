# link: https://leetcode.com/submissions/detail/746783399/
def letter_combinations(digits):
    """
    for a string consisting of digits chosen from 2 to 9 (repeatition allowed),
    this function finds all possible letter combinations that the number could
    represent according telephone string-to-number encoder.

    Example:
    letterCombinations("23"):
    ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    (2 is "abc", 3 represents "def")

    Parameters
    ----------
    digits : str
        a string of digits, where each digit can be any number from 2(inclusive)
        to 9(inclusive)

    Returns
    -------
    lst : List
        a list of strings where each string can be represnted by `digits`
    """

    def letter_combinations_helper(digits, lst, mapper):
        if len(digits) == 0:
            return lst
        else:
            d = digits[-1]
            if len(lst) == 0:
                lst = [""]

            lst_new = []
            for item in lst:
                for s in mapper[d]:
                    lst_new.append(s + item)

        return letter_combinations_helper(digits[:-1], lst_new, mapper)

    mapper = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    lst = letter_combinations_helper(digits, [], mapper)

    return lst


# cleaner?
