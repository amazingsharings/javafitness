/*
    problem: Reverse Integer
    author: everpuck
    date: 2/14/2019
*/


class Solution {
    public int reverse(int x) {
        // StringBuilder ret = new StringBuilder (Integer.toString(x));
        StringBuffer ret = new StringBuffer  (Integer.toString(x));
        ret.reverse();
        int iret = 0;

        try
        {
            if (x < 0) {
                iret = -1 * Integer.parseInt(ret.substring(0, ret.length()-1));
            }
            else {
                iret = Integer.parseInt(ret.toString());
            }
        }
        catch (Exception e)
        {
            return 0;
        }
        return iret;
    }
}

public class ReverseInteger {
    public static void main(String[] args) {
        // int x = 2147483647;
        int x = -10200;
        Solution solution = new Solution();
        int ret = solution.reverse(x);
        System.out.println(ret);
    }
}