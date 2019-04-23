# problem: Reverse Integer
# author: everpuck
# date: 2/14/2019


class Solution:
    def reverse(self, x: 'int') -> 'int':
        if x == 0:
            return x
        xlist = list(str(x).strip('0'))
        if x < 0:
            xlist  = xlist  [1:]
        for i in range(len(xlist)//2):
            xlist[i], xlist[-(i + 1)] = xlist[-(i + 1)], xlist[i]
        
        ret = int("-" + "".join(xlist) if x < 0 else "".join(xlist))
        if ret < -2**31 or ret > 2**31 -1:
            return 0
        return ret


if __name__ == '__main__':
    x = 0
    solution = Solution()
    print(solution.reverse(x))
