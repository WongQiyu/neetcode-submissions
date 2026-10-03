# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #store slow.next
        second = slow.next
        prev = slow.next = None

        #Loop second half and reverse
        while second:
            #store next value
            tmp = second.next
            #reverse where current node next value is prev
            second.next = prev
            #continue loop such that previous node is current node
            prev = second
            #continue loop on next node, which was previously stored
            second = tmp
        # where second is start node of second half after reverse
        first, second = head, prev
        while second:
            # temporarily store the next node for looping
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            # continue to loop
            first, second = tmp1, tmp2


        