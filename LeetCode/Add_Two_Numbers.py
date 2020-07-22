#time complexity:O(n)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Example:

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807




class Solution(object):
    def addSum(l1, l2):
        carry = 0
        newList = Node(0)
        tmp = newList
        totalSum = 0

        while l1 or l2:
            if l1:
                totalSum += l1.val
                l1 = l1.next
            if l2:
                totalSum += l2.val
                l2 = l2.next
                totalSum += carry
                tmp.next = Node(totalSum % 10)
                carry = totalSum/10
                tmp = tmp.next


        return newList.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ## RC ##
        # 1. if two lists are unequal place 0 node.
        # 2. forward carry to next node.
        # 3. check last carry edge condition, append if carry exists.
        
        ans = ListNode(0)
        temp = ans
        carry = 0
        while(l1 or l2):
            if(not l1):
                l1 = ListNode(0)
            elif(not l2):
                l2 = ListNode(0)
            sm = l1.val + l2.val + carry
            if(sm >= 10):
                carry = 1
                temp.next = ListNode(sm-10)
            else:
                carry = 0
                temp.next = ListNode(sm)  
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        if(carry > 0):          # watchout
            temp.next = ListNode(carry)        
        return ans.next
