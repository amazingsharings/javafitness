# Median of Two Sorted Arrays

## [原文](https://leetcode.com/problems/median-of-two-sorted-arrays/)

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

**Example 1:**

``` text
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
```

**Example 2:**

``` text
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
```

## 翻译

大概是有俩长度分别为m 和n的有序数组，找出俩数组的*中间值*，时间复杂度要求O(log (m+n))，假定俩数组都不为空。

> + 根据例子，大概题目要求的中间值简单来讲，是先将俩列表合并，然后拿到新的有序列表的中间的值，如果中间的值是俩个的话，则求平均值。
> + 当然如果真的先合并再求中间值的话，时间复杂度肯定不符合要求。
> + 该题难度等级为**hard**
