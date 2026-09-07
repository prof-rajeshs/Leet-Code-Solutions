class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        # Helper function to compute distances from a starting node
        def get_distances(start_node: int) -> list[int]:
            distances = [-1] * n
            dist = 0
            curr = start_node
            while curr != -1 and distances[curr] == -1:
                distances[curr] = dist
                dist += 1
                curr = edges[curr]
            return distances

        # Get distances from both nodes
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)
        
        min_max_dist = float('inf')
        ans_node = -1
        
        # Find the node that minimizes the maximum distance
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                current_max = max(dist1[i], dist2[i])
                if current_max < min_max_dist:
                    min_max_dist = current_max
                    ans_node = i
                    
        return ans_node
