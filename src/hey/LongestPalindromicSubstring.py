# problem: Longest Palindromic Substring 
# author: everpuck
# date: 2/2/2019


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 2:
            return s
        
        max_index = 0
        max_length = 0
        is_odd = True
        length = len(s)
        for i in range(length):

            for j in range(i):
                if i + j + 1>= length or s [i + j + 1] != s[i - j -1]:
                    break
                if j + 1 > max_length:
                    max_length, max_index , is_odd = j + 1, i, True
            
            if i + 1 < length and s[i] == s[i+1]:
                for j in range(i):
                    if i + j + 2 >= length or s [i + j + 2] != s[i - j - 1]:
                        break
                    if j + 1 >= max_length:
                        max_length, max_index, is_odd = j + 1, i, False
            # elif i + 1 < length and s[i] != s[i + 1]:
            #     continue
        
            if i + 1 < length and s[i] == s[i+1] and max_length < 1:
                max_index, is_odd = i, False

        if is_odd:
            ret = s[max_index - max_length: max_index + max_length + 1]
        else:
            ret = s[max_index - max_length: max_index + max_length + 2]
        
        return ret


if __name__ == '__main__':
    s = 'sbabbad'
    # s = 'bbd'
    s = 'aaaa'
    # s = "aaabaaaa"
    # s = 'aaaabaa'
    solution = Solution()
    print(solution.longestPalindrome(s))
