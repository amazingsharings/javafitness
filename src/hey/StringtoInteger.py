# problem: String to Integer (atoi)
# author: everpuck
# date: 2/15/2019


class Solution:
    def myAtoi(self, str: 'str') -> 'int':
        ret_str = str.lstrip(' ')
        ret = 0
        sign = 1
        for i, c in enumerate(ret_str):
            if i == 0:
                if c == "-":
                    sign = -1
                elif c == "+":
                    continue
                elif c.isdigit():
                    ret = int(c)
                else:
                    return 0
            else:
                if c.isdigit():
                    ret = ret*10 + int(c)
                else:
                    break
        ret *= sign
        min_value = -2**31
        max_value = 2**31 - 1
        if ret < min_value:
            return min_value
        elif ret > max_value:
            return max_value
        return ret


if __name__ == '__main__':
    _str = 'words and 987'
    _str = '4193 with words'
    _str = '    -042'
    _str = ''
    solution = Solution()
    print(solution.myAtoi(_str))

