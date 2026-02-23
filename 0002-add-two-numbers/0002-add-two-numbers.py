# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2=[]
        
        while l1:
            arr1.append(l1.val)
            l1 = l1.next
        while l2:
            arr2.append(l2.val)
            l2 = l2.next
        n1="".join(map(str, arr1))[::-1]
        n2="".join(map(str, arr2))[::-1]

        sum=int(n1)+int(n2)
        sum=str(sum)[::-1]
        
        dummy = ListNode()      # keep head safe
        curr = dummy            # moving pointer

        for digit in sum:
            curr.next = ListNode(int(digit))   # convert to int
            curr = curr.next

        return dummy.next