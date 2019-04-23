# problem: Reverse Integer
# author: everpuck
# date: 2/16/2019


class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0:
            return False
        digit_list = []
        while x != 0:
            digit_list.append(x % 10)
            x //= 10
        digit_list_copy = digit_list.copy()
        digit_list_copy.reverse()
        return digit_list == digit_list_copy

    def isPalindrome2(self, x: 'int') -> 'bool':
        if x < 0:
            return False
        digit_list = []
        while x != 0:
            digit_list.append(x % 10)
            x //= 10
        
        for i in range(len(digit_list)//2):
            if digit_list[i] != digit_list[-(i + 1)]:
                return False
        return True



if __name__ == '__main__':
    x = 12321
    solution = Solution()
    print(solution.isPalindrome2(x))