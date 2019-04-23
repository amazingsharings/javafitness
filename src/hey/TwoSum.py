# problem: two sum
# author: everpuck
# date: 1/31/2019


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        for i, num in enumerate(nums):
            o_num = target - num
            if o_num in nums[i+1:]:
                ret.extend([i, nums[i+1:].index(o_num) + i+1])
                break
        return ret
        

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target))
