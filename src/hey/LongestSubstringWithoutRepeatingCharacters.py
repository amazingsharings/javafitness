# problem: Longest Substring Without Repeating Characters
# author: everpuck
# date: 2/2/2019


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_list = []
        ret = 0
        for c in s:
            if c in sub_list:
                ret = max(len(sub_list), ret)
                sub_list = sub_list[sub_list.index(c) + 1: ]
                sub_list.append(c)
            else:
                sub_list.append(c)
        
        ret = max(len(sub_list), ret)
        return ret


if __name__ == '__main__':
    s = 'abcabcbb'
    s = 'pwwkew'
    s = 'bbb'
    s = 'dvdf'
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
