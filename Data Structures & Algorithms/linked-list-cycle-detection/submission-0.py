# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(n) time & O(1) space
        slow, fast = head, head

        while fast and fast.next: # while fast is not null and fast.next is not null
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # if slow ever reaches fast
                return True

        return False