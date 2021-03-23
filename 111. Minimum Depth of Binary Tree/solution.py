# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        queue.append(root)
        ans = 1
        while len(queue) :
            s = len(queue)
            while s:
                a = queue.pop(0)
                
                if a.left:
                    
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
                if not a.left and not a.right:
                    return ans
                
                s -= 1
            ans += 1
