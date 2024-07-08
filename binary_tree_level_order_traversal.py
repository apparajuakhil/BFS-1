"""
# BFS-1
# Problem 1
Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)

Time Complexity : O(n)
Space Complexity : O(n) ~ diameter of the tree
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

Your code here along with comments explaining your approach:
Trick is to understand that we append the root to queue initially and then pop the root and append it's children and then again
we loop over the current size of queue which has children in it, then we pop each children and again push the popped nodes children. 
Also, we  need to make sure once we complete the inner loop we need to push the current list that we stored in the inner loop to push 
into the final resultant list as it contains each level elements.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque()
        queue.append(root)

        result = []

        while len(queue) > 0:
            size = len(queue)
            level_nodes = []
            for i in range(size):
                popped_node = queue.popleft()

                if popped_node.left:
                    queue.append(popped_node.left)
                if popped_node.right:
                    queue.append(popped_node.right)

                level_nodes.append(popped_node.val)

            result.append(level_nodes)

        return result
                

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # T.C O(n) S.C O(h)
        if not root:
            return []
        
        result = []
        def dfs(root, level):
            if root is None:
                return 

            if level == len(result):
                result.append([])

            result[level].append(root.val)

            dfs(root.left, level+1)
            dfs(root.right, level+1)

        dfs(root, 0)
        return result

        