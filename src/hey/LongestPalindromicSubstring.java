/*
    problem: Median of Two Sorted Arrays
    author: everpuck
    date: 02/10/2019
*/

class Solution {
    public String longestPalindrome(String s) {
        int length = s.length();
        int maxIndex = 0;
        int maxLength = 0;
        boolean isOdd = true;
        for (int i = 0; i < length; ++i) {
            for (int j = 0; j < i; ++j) {
                if (i + j + 1 >= length || s.charAt(i + j + 1) != s.charAt(i - j - 1)) {
                    break;
                }
                if (j + 1 > maxLength) {
                    maxLength = j + 1;
                    maxIndex = i;
                    isOdd = true;
                }
            }
            if (i + 1 < length && s.charAt(i) == s.charAt(i+1)) {
                for (int j = 0; j < i; ++j) {
                    if (i + j + 2 >= length || s.charAt(i + j + 2) != s.charAt(i - j - 1)) {
                        break;
                    }
                    if (j + 1 >= maxLength) {
                        maxLength = j + 1;
                        maxIndex = i;
                        isOdd = false;
                    }
                }
            }
            if (i + 1 < length && s.charAt(i) == s.charAt(i+1) && maxLength < 1) {
                maxIndex = i;
                isOdd = false;
            }
        }
        if (length < 1) {
            return "";
        }
        if (isOdd) {
            return s.substring(maxIndex - maxLength, maxIndex + maxLength + 1);
        }
        else {
            return s.substring(maxIndex - maxLength, maxIndex + maxLength + 2);
        }
        
    }
}


public class LongestPalindromicSubstring {
    public static void main(String[] args) {
        String retString = "";
        // String s = new String("babad");
        // String s = new String("cbbd");
        // String s = new String("aaaabaa");
        String s = new String("");
        Solution solution = new Solution();
        retString = solution.longestPalindrome(s);
        System.out.println(retString);
    }
}