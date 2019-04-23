/*
    problem: Reverse Integer
    author: everpuck
    date: 2/16/2019
*/

import java.util.*;

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        List<Integer> list = new ArrayList<Integer>();
        while (x > 0) {
            list.add(x % 10);
            x = x / 10;
        }
        for (int i = 0; i < list.size()/2; i++) {
            if (list.get(i) != list.get(list.size()-i-1)) {
                return false;
            }
        }
        return true;
    } 
}


public class PalindromeNumber {
    public static void main(String[] args) {
        int x = 12321;
        Solution solution = new Solution();
        System.out.println(solution.isPalindrome(x));
    }
}
