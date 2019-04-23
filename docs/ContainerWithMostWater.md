# Container With Most Water

## [原文](https://leetcode.com/problems/container-with-most-water/)

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

**Note:** You may not slant the container and n is at least 2.

> ![avatar](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)
> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

**Example:**

``` text
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

## 翻译

给n个非负整数，a1, a2, ..., an, 每一个代表一个坐标系中的点（i, ai），n条垂直线被画在坐标系上，一条线段的俩端点是（i, ai）和（i, 0）。找出两条线，要求这两条线组成一个容器，且这个容器能盛最多的水。

**注意：** 你不能倾斜这个容器（理解为最终是容器形状是矩形，不能是梯形），且n最小是2。