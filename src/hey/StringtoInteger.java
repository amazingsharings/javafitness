/*
    problem: String to Integer (atoi)
    author: everpuck
    date: 2/16/2019
*/


class Solution {
    public int myAtoi(String str) {
        String trimStr = str.trim();
        int sign = 1;
        double ret = 0;

        for (int i = 0; i < trimStr.length(); i++) {
            if (i == 0) {
                if (trimStr.charAt(i) == '-') {
                   sign = -1;
                }
                else if (trimStr.charAt(i) == '+') {
                    continue;
                }
                else if (trimStr.charAt(i) > 47 && trimStr.charAt(i) < 58) {
                    ret = trimStr.charAt(i) - 48;
                }
                else {
                    return 0;
                }
            }
            else {
                if (trimStr.charAt(i) > 47 && trimStr.charAt(i) < 58) {
                    ret = ret * 10 + trimStr.charAt(i) - 48;
                }
                else {
                    break;
                }
            }
        }
        ret *= sign;
        if (ret < Integer.MIN_VALUE) {
            ret = Integer.MIN_VALUE;
        }
        if (ret > Integer.MAX_VALUE) {
            ret = Integer.MAX_VALUE;
        }
        return (int)ret;
    }
}


public class StringtoInteger {
    public static void main(String[] args) {
        // String str = " +-0123abc0";
        // String str = " -01239abc0";
        // String str = "      +123abc0";
        // String str = " ";
        // String str = "-2147483649";
        String str = "9223372036854775808";
        Solution solution = new Solution();
        int ret = solution.myAtoi(str);
        System.out.println(ret);
    }
}
