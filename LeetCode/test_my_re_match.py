# link: https://leetcode.com/problems/regular-expression-matching/

def move_star(p):
    """
    shifting character "*" in the string * until its next character becomes
    differenet than its previous one!

    Example: "aa*aaab" --> "aaaaa*b"
    """
    if len(p) <= 2:
        return p

    p_lst = list(p)

    i = 1
    while i < len(p) - 1:
        if p_lst[i] != "*":
            i += 1
            continue
        chr = p_lst[i - 1]
        for j in range(i + 1, len(p)):
            if p_lst[j] != chr:
                break
        p_lst[i] = chr
        p_lst[j - 1] = "*"

        i = j

    p = "".join(p_lst)

    return p


def naive_my_re_match(s, p):
    # move * such that it appears at end of a block of same letters
    # aa*aaaba --> aaaaa*ba

    p = move_star(p)

    si = 0
    pj = 0

    for _ in range(max(len(s), len(p))):
        if si >= len(s) or pj >= len(p):
            break # analyze this case later

        if s[si] == p[pj]:
            continue

        if p[pj] == '.':
            continue

        if p[pj] != '*':
            return False
        else:
            # p[pj] is '*'
            # ???


    #To Be continued!
