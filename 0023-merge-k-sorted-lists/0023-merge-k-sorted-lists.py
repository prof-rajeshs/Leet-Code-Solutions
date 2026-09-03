import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Dummy node acts as the start of the merged linked list
        dummy = ListNode(0)
        current = dummy
        
        # Min-heap stores tuples: (node_value, unique_id, node_object)
        # unique_id prevents comparison errors when two nodes have identical values
        heap = []
        
        # Initialize the heap with the head node of each non-empty list
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
                
        # Process the heap until all nodes are merged
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Append the smallest node to the merged list
            current.next = node
            current = current.next
            
            # If the extracted node has a next node, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
