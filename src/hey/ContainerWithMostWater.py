# problem: Container With Most Water
# author: everpuck
# date: 4/24/2019


class Solution:
    # 暴力遍历
    # Time Limit Exceeded!!!
    def maxArea_bad(self, height: 'List[int]') -> 'int':
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                if (j - i) * min(height[i], height[j]) > max_area:
                    max_area = (j - i) * min(height[i], height[j])
        return max_area

    def maxArea(self, height: 'List[int]') -> 'int':
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(height))
