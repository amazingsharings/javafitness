/*
    problem: Median of Two Sorted Arrays
    author: everpuck
    date: 02/09/2019
*/


class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int index1 = 0;
        int index2 = 0;
        // double[] target_value = new double[2];
        double targetValue = 0.0d;
        int tempValue = 0;

        int targetIndex = (nums1.length + nums2.length) / 2;
        boolean isUnique = false;

        if ((nums1.length + nums2.length) % 2 > 0) {
            isUnique = true;
        }
        // System.out.println("targeIndex: " + targetIndex);
        // System.out.println("isUnique: " + isUnique);
        while (true) {
            if (index1 < nums1.length && index2 < nums2.length) {
                if (nums1[index1] < nums2[index2]) {
                    tempValue = nums1[index1++];
                } 
                else {
                    tempValue = nums2[index2++];
                }
            }
            else if (index1 < nums1.length) {
                tempValue  = nums1[index1++];
            }
            else if (index2 < nums2.length) {
                tempValue = nums2[index2++];
            }
            // else {
            //     break;
            // }
            if (isUnique && index1 + index2 > targetIndex) {
                targetValue = tempValue;
                break;
            }
            else if (!isUnique) {
                if (index1 + index2 >= targetIndex) {
                    targetValue += tempValue;
                }
                if (index1 + index2 >= targetIndex + 1) {
                    break;
                }
            }
        }
        if (!isUnique) {
            return targetValue / 2;
        }
        return targetValue;
    } 
}

public class MedianofTwoSortedArrays {
    public static void main(String[] args) {
        double ret = 0;
        int[] nums1 = {};
        int[] nums2 = {2};
        Solution solution = new Solution();
        ret = solution.findMedianSortedArrays(nums1, nums2);
        System.out.println("MedianofTwoSortedArrays ret: " + ret);
    }
}