#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        joints = {}
        for row in wall:
            curr = 0
            for brick in row:
                curr += brick
                joints[curr] = joints.get(curr, 0) + 1
        joints.pop(sum(wall[0]))

        minCross = len(wall)
        for _, count in joints.items():
            minCross = min(len(wall) - count, minCross)
        return minCross
# @lc code=end

