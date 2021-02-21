# https://leetcode-cn.com/problems/check-permutation-lcci/submissions/
class Solution(object):
    def CheckPermutation(self, s1, s2):
        # length should be the same
        if (len(s1) != len(s2)):
            return False

        # sort those two array nlogn
        # https://stackoverflow.com/questions/15046242/how-to-sort-the-letters-in-a-string-alphabetically-in-python
        s1 = ''.join(sorted(s1))
        s2 = ''.join(sorted(s2))

        length = len(s1)
        i = 0
        while i < length:
            if (s1[i] != s2[i]):
                return False
            else:
                i = i + 1
        return True 