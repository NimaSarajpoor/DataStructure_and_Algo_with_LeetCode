# link: https://leetcode.com/problems/3sum/
def three_sum(nums):
        """
        For a list  of integers, return all triples whose sum is 0.

        Example:
        three_sum([0, 0, 0]):
        >>> [[0, 0, 0]]

        three_sum([0, 1, 2]):
        >>> []

        three_sum([0, 0, -1, 2, 1]):
        >>> [[0, -1, 1], [-1, 2, 1]]

        Parameters
        ----------
        nums : list
            a list with minimum length of 3, consisting of integers

        Returns
        -------
        out: list
            a list with members that are lists with length three. Each inner list
            consists of three numbers that are in `nums`, and their sum is 0.
        """

        cnts = Counter(nums)
        unique_values = list(cnts.keys())
        unique_values.sort()

        out = []
        visited = [False] * len(unique_values)
        for idx, v in enumerate(unique_values):
            target = -v
            i = 0
            j = len(unique_values) - 1
            while i <= j:
                if unique_values[i] + unique_values[j] < target:
                    i += 1
                    continue
                elif unique_values[i] + unique_values[j] > target:
                    j -= 1
                    continue
                elif visited[i] or visited[j]:
                    i += 1
                    j -= 1
                    continue
                else:
                    lst = [v, unique_values[i], unique_values[j]]
                    eligible=True
                    for key, item in Counter(lst).items():
                        if item > cnts[key]:
                            eligible = False
                            break
                    if eligible:
                        out.append(lst)

                    i += 1
                    j -= 1

            visited[idx] = True

        return out
