from typing import ListNode
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: 
        nodes_in_B = set()

        while headB is not None:   # Add nodes B into hash table
            nodes_in_B.add(headB)
            headB = headB.next

        while headA is not None:   # Check whether any of the nodes A is in the hash table
            # if we find the node pointed to by headA,
            # in our set containing nodes of B, then return the node
            if headA in nodes_in_B:
                return headA
            headA = headA.next

        return None     