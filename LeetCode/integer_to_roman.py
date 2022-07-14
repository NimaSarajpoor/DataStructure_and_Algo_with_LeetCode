# link: https://leetcode.com/problems/integer-to-roman/
def integer_to_roman(num):
    map_to_roman = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }

    keys = list(map_to_roman.keys())
    for i in keys:
        if i in [1, 10, 100]:
            for j in keys:
                if j > i and j <= i * 10:
                    map_to_roman[j-i] = map_to_roman[i] + map_to_roman[j]

    keys = list(map_to_roman.keys())
    keys.sort(reverse = True)
    r = num

    s = ""
    for k in keys:
        if r == 0:
            break

        if r in map_to_roman:
            s = s + map_to_roman[r]
            break

        n = r // k
        if n == 0:
            continue

        s = s + n * map_to_roman[k]
        r = r - n * k

    return s
