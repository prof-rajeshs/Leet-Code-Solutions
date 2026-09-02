class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # Step 1: Calculate the height of the tree
        def getHeight(node):
            if not node:
                return-1
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        height = getHeight(root)
        
        # Step 2: Initialize the matrix dimensions
        m = height + 1
        n = (2 ** (height + 1)) - 1
        res = [[""] * n for _ in range(m)]
        
        # Step 3: Populate the matrix using DFS
        def fill(node, r, c):
            if not node:
                return
            res[r][c] = str(node.val)
            
            # Calculate column offset for children
            offset = 2 ** (height - r - 1)
            
            if node.left:
                fill(node.left, r + 1, c - offset)
            if node.right:
                fill(node.right, r + 1, c + offset)
                
        fill(root, 0, (n - 1) // 2)
        return res
