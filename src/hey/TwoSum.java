/*
    problem: two sum
    author: everpuck
    date: 1/31/2019
*/


class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ret = new int[2];
        for (int i = 0; i < nums.length - 1; ++i) {
            for (int j = i+1; j< nums.length; ++j) {
                if (nums[i] + nums[j] == target) {
                    ret[0] = i;
                    ret[1] = j;
                    break;
                } 
            }
            if (ret[1] > 0) {
                break;
            }
        }
        return ret;
    }
}


public class TwoSum {
    public static void main(String[] args) {
        int[] nums = new int[]{2, 7, 11, 15}; 
        int target = 9;
        int[] ret;
        Solution solution = new Solution();
        ret = solution.twoSum(nums, target);
        if (ret.length > 1) {
            System.out.println("twoSum result: " + ret[0] + ", " + ret[1]);
        }
        else {
            System.out.println("twoSum no result");
        }
    }
}