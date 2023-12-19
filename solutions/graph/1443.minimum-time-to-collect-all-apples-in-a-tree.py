#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#

# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = {i:[] for i in range(n)}
        for src, dst in edges:
            tree[src].append(dst)
            tree[dst].append(src)
        
        def dfs(curr, prev):
            edgeSum = 0
            for node in tree[curr]:
                if node == prev:
                    continue
                edgeSum += dfs(node, curr)
            if curr != 0 and (edgeSum or hasApple[curr]):
                edgeSum += 2
            return edgeSum
        
        return dfs(0, -1)
     
# @lc code=end

