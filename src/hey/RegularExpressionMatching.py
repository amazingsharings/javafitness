# problem: Regular Expression Matching
# author: everpuck
# date: 2/16/2019


"""
题目难度是hard，以下是官方参考答案之一，虽然速度很慢- -！
"""


class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


if __name__ == '__main__':
    s = "miss issippi"
    p = "mis*is*p*."
    s = "ab"
    p = ".*"
    s = "a"
    p = ".*..a*"

    s = "ab"
    p = ".*..c*"
    s = 'aa'
    p = 'a'
    s = 'ab'
    p = '.*'

    solution = Solution()
    print(solution.isMatch(s, p))
