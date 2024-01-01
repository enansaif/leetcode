#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#

# @lc code=start
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node, visited):
            visited, dist = {}, 0
            while node != -1:
                if node in visited:
                    break
                visited[node] = dist
                node = edges[node]
                dist += 1
            return visited
        
        dstNode1 = dfs(node1, {})
        dstNode2 = dfs(node2, {})
        
        res, resDist = -1, float("inf")
        for i in range(len(edges)):
            if i in dstNode1 and i in dstNode2:
                dist = max(dstNode1[i], dstNode2[i])
                if dist < resDist:
                    resDist = dist
                    res = i
        return res
        
# @lc code=end

