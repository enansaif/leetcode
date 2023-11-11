#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0 for _ in range(len(graph))]
        def bfs(node):
            if color[node] != 0:
                return True

            q = deque([node])
            color[node] = -1

            while q:
                node = q.popleft()
                for nbr in graph[node]:
                    if color[node] == color[nbr]:
                        return False
                    if color[nbr] == 0:
                        q.append(nbr)
                    color[nbr] = -1*color[node]
            return True
        
        for n in range(len(graph)):
            if bfs(n) == False:
                return False
        return True
        
# @lc code=end

