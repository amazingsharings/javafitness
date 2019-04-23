# problem: Median of Two Sorted Arrays
# author: everpuck
# date: 2/2/2019


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # if not nums2:
        #     pass
        # elif not nums1 or nums1[0] < nums2[0]:
        #     nums1, nums2 = nums2, nums1
        med_index = (len(nums1) + len(nums2)) / 2
        if (len(nums1) + len(nums2)) % 2 == 0:
            med_index = [int(med_index-1), int(med_index)]
        else:
            med_index = [int(med_index), ]
        med_val = [] 
        tem_index = 0
        index2 = 0
        length2 = len(nums2)
        big_flag = False

        for num1 in nums1:
            if len(med_val) == len(med_index):
                break
            while 1:
                if index2 > length2 - 1:
                    big_flag = True
                    break
                if num1 >= nums2[index2]:
                    if tem_index in med_index:
                        med_val.append(nums2[index2])
                    index2 += 1
                    tem_index += 1
                    if len(med_val) == len(med_index):
                        break
                else:
                    big_flag = True
                    break
            # 内存循环退出标识
            if big_flag:
                if tem_index in med_index:
                    med_val.append(num1)
                big_flag = False
                tem_index += 1
            
        if len(med_val) < len(med_index):
            for num2 in nums2[index2:]:
                if tem_index in med_index:
                    med_val.append(num2)
                if len(med_val) == len(med_index):
                    break
                tem_index += 1

        return sum(med_val) / len(med_val)



if __name__ == '__main__':
    nums1 = [6, 7]
    nums2 = []
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))
    print('this problem is really too hard!')
