# ZigZag Conversion

## [原文](https://leetcode.com/problems/zigzag-conversion/)

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

``` text
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

> string convert(string s, int numRows);

**Example 1:**

``` text
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```text
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

## 翻译

第一眼看不懂:(

重点在'zigzag pattern'的理解，字面为'锯齿模式'，其实类似大写字母‘N’(要从背面看)，题意应该是将字符串按照'zigzag pattern'模式排列，然后顺序打印，并且去掉所有空格及换行等。