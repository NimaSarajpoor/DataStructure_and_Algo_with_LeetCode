

def naive_my_re_match(s, p):
    # move * such that it appears at end of a block of same letters
    # aa*aaaba --> aaaaa*ba

    def move_star(p):
        if len(p) > 2: #so, we might have "*" that can be moved!
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

    p = move_star(p)

    # TBC
