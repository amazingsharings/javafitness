# Regular Expression Matching

## [原文](https://leetcode.com/problems/regular-expression-matching/)

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

``` text
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
```

The matching should cover the entire input string (not partial).

**Note:**

+ s could be empty and contains only lowercase letters a-z.
+ p could be empty and contains only lowercase letters a-z, and characters like . or *.

**Example 1:**

``` text
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:**

``` text
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

**Example 3:**

``` text
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

**Example 4:**

``` text
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
```

**Example 5:**

``` text
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
```

## 翻译

输入一个字符串（s）和一个模式（p），实现支持‘.’或者‘*’的正则表达式匹配。

``` text
‘.’匹配任意单个字符。
‘*’匹配0个或者多个之前的字符。
```

**注意:**

+ s可以为空以及包含所有小写的字母a-z。
+ p可以为空以及包含所有的小写字母a-z，和字符.或者*。
