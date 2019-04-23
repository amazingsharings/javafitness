/*
    problem: Regular Expression Matching
    author: everpuck
    date: 2/19/2019
*/


class Solution {
    // official answer
    public boolean isMatch(String s, String p) {
        if (p.isEmpty()) {
            return s.isEmpty();
        }
        boolean first_match = (!s.isEmpty() &&
                               (p.charAt(0) == s.charAt(0) || p.charAt(0) == '.'));
        if (p.length() >= 2 && p.charAt(1) == '*'){
            return (isMatch(s, p.substring(2)) ||
                    (first_match && isMatch(s.substring(1), p)));
        } else {
            return first_match && isMatch(s.substring(1), p.substring(1));
        }
    }
}


public class RegularExpressionMatching {
    public static void main(String[] args) {
        String s = "miss issippi";
        String p = "mis*is*p*.";
        Solution solution = new Solution();
        System.out.println(solution.isMatch(s, p));
    }
}
