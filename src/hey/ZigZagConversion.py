# problem: ZigZag Conversion
# author: everpuck
# date: 02/11/2019

"""
如果按照用二维数组存储的话，关于行数和列数大概思考了下，有以下结论：
1. 数组行数等于题目要求numRows
2. 数组列数需要计算:
        if int(len(s)/(2*numRows-2)) > 0:
            if len(s)%(2*numRows-2) == 0:
                numColumns = int(len(s)/(2*numRows-2)) * (numRows-1)
            elif len(s)%(2*numRows-2) <= numRows:
                numColumns = int(len(s)/(2*numRows-2)) * (numRows-1) + 1
            else:
                numColumns = int(len(s)/(2*numRows-2)) * (numRows-1) + len(s)%(2*numRows-2) - numRows + 1
        else:
            if len(s) <= numRows:
                numColumns = 1
            else:
                numColumns = len(s) % numRows + 1
3. 按列打印，当列数为numRows-1的整数倍时候顺序依次打印满列，否则该列只打印一个，行号为上一行行号-1
4. 这个方法速度太慢！！！
"""

class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        if numRows < 2:
            return s
        # s = s.replace(' ', '#')
        if int(len(s)/(2*numRows-2)) > 0:
            if len(s)%(2*numRows-2) == 0:
                numColumns = int(len(s)/(2*numRows-2)) * (numRows-1)
            elif len(s)%(2*numRows-2) <= numRows:
                numColumns = int(len(s)/(2*numRows-2)) * (numRows-1) + 1
            else:
                numColumns = int(len(s)/(2*numRows-2)) * (numRows-1) + len(s)%(2*numRows-2) - numRows + 1
        else:
            if len(s) <= numRows:
                numColumns = 1
            else:
                numColumns = len(s) % numRows + 1
        # element stores column line
        ret_sequence = [[] for i in range(numColumns)]
        s_index = 0
        col_index = 0
        for j in range(numColumns):
            for i in range(numRows):
                
                if s_index >= len(s):
                    c = "_"
                else:
                    c = s[s_index]
                if j % (numRows - 1) == 0:
                    ret_sequence[j].append(c)
                    s_index += 1
                    col_index = i - 1
                else:
                    if i == col_index:
                        ret_sequence[j].append(c)
                        s_index += 1
                        col_index -= 1
                    else:
                        ret_sequence[j].append("_")
        ret_str = ""
        index = 0
        i = 0
        while i < numRows:
            for row in ret_sequence:
                if i < len(row) and row[i] != "_":
                    ret_str += row[i]
                    index += 1
            i += 1

        return ret_str
    
    # 速度很快，但是也很占用空间
    def convert_official(self, s: 'str', numRows: 'int') -> 'str':
        if numRows == 1:
            return s
        ret_sequence = [""] * min(numRows, len(s));
        going_down = False
        cur_row = 0
        for  c in s:
            ret_sequence[cur_row] += c
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            if going_down:
                cur_row += 1
            else:
                cur_row += -1
        
        return "".join(ret_sequence)

    """
    java version
    class Solution {
    public String convert(String s, int numRows) {

            if (numRows == 1) return s;

            StringBuilder ret = new StringBuilder();
            int n = s.length();
            int cycleLen = 2 * numRows - 2;

            for (int i = 0; i < numRows; i++) {
                for (int j = 0; j + i < n; j += cycleLen) {
                    ret.append(s.charAt(j + i));
                    if (i != 0 && i != numRows - 1 && j + cycleLen - i < n)
                        ret.append(s.charAt(j + cycleLen - i));
                }
            }
            return ret.toString();
        }
    }
    """
    # 直接算下标顺序赋值
    def convert_official2(self, s: 'str', numRows: 'int'):
        if numRows == 1:
            return s
        ret = ""
        length = len(s)
        cycle_len = 2 * numRows - 2
        for i in range(numRows):
            j = 0
            while 1:
                ret += s[i + j]
                if i != 0 and i != numRows -1 and j + cycle_len - i < length:
                    ret += s[j + cycle_len -i]
                j += cycle_len
                if j + i >= length:
                    break
        return ret

    # 这个方法看不懂 :(
    def convert_other(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
       
        if numRows == 1 or numRows >= len(s):
            return s

        n=numRows
        z=['']*n
        rn=list(range(0,n-1))+ list(range(n-1,0,-1))
        print(repr(rn))
        s_len=len(s)
        i=0 # character number       
        for l in range(s_len//(2*n-2)+1): # loop number. this will chang the column number
            for j in range(2*n-2):
                z[rn[j]]+=s[i]
                if i == (s_len -1):
                    return "".join(z)   
                else:
                    i=i+1


if __name__ == '__main__':
    # numRows = 4 
    numRows = 10 
    # s = 'PAYPALISHIRING'
    s = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."
    # s = 'PAYPA'
    solution = Solution()
    print(solution.convert(s, numRows))
    print(solution.convert_official(s, numRows))
    print(solution.convert_official2(s, numRows))
    print(solution.convert_other(s, numRows))
        