# link: https://leetcode.com/problems/longest-common-prefix/
def longest_common_prefix(strs):
    best_so_far = strs[0]
    for word in strs[1:]:
        i = 0
        for _ in range(min(len(best_so_far), len(word))):
            if best_so_far[i] != word[i]:
                break
            i += 1

        best_so_far = word[:i]

    return best_so_far
