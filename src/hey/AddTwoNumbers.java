/*
    problem: add two numbers
    author: everpuck
    date: 2/1/2019
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}


class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode curNode = head;
        int val = 0;
        int nodeVal = 0;
        boolean need_carry = false;
        while (l1 != null || l2 != null) {
            val = 0;
            nodeVal = 0;

            if (need_carry) {
                val = 1;
            }
            if (l1 != null) {
                val += l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                val += l2.val;
                l2 = l2.next;
            }

            if (val > 9) {
                need_carry = true;
                nodeVal = val - 10;
            }
            else {
                need_carry = false;
                nodeVal = val;
            }

            curNode.next =  new ListNode(nodeVal);
            curNode = curNode.next;
        }
        if (need_carry) {
            curNode.next =  new ListNode(1);
        }
        return head.next;
    }
}


public class AddTwoNumbers {
    public static void main(String[] args) {
        System.out.println("hello world");
    }
}
