# problem: add two numbers
# author: everpuck
# date: 1/31/2019


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret_head = None
        cur = None
        need_carry = False
        while 1:
            val = 0
            if need_carry:
                val = 1

            if l1 and l2:
                val += l1.val + l2.val
                l1, l2 = l1.next, l2.next
            elif l1:
                val += l1.val
                l1 = l1.next
            elif l2:
                val += l2.val
                l2 = l2.next
            # end if last number is zero
            elif val == 0:
                break

            node_val = 0
            if val > 9:
                need_carry, node_val = True, val - 10
            else:
                need_carry = False
                node_val = val

            temp_node = ListNode(node_val)
            
            if not cur:
                ret_head = temp_node
                cur = temp_node
            else:
                cur.next = temp_node
                cur = cur.next

        return ret_head


if __name__ == '__main__':
    pass
