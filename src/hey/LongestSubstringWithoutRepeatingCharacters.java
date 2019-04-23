/*
    problem: Median of Two Sorted Arrays
    author: everpuck
    date: 02/09/2019
*/


class Solution {
    public int lengthOfLongestSubstring(String s) {
        String tempString = "";
        int ret = 0;
        char c;
        for (int i = 0; i < s.length(); ++i) {
            c = s.charAt(i);
            if (tempString.length() > 0 && 
                tempString.indexOf(c) > -1) {
                ret = Math.max(tempString.length(), ret);
                tempString = tempString.substring(tempString.indexOf(c) + 1);
                tempString += c;
            }
            else {
                tempString += c;
            }
        }
        ret = Math.max(tempString.length(), ret);
        return ret;
    }

    /* Official sliding window algrorithm
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));
            }
        }
        return ans;
    }
    */

}


public class LongestSubstringWithoutRepeatingCharacters {
    public static void main(String[] args) {
        int ret = 0;
        String s = new String("cdd");
        Solution solution = new Solution();
        ret = solution.lengthOfLongestSubstring(s);
        System.out.println(" ret: " + ret);
    }
}