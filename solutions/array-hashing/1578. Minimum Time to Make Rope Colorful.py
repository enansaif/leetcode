#Question Link: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prevClr, minTime = 0, 0
        currMax, currSum = 0, 0
        for i, c in enumerate(colors):
            if c != prevClr:
                minTime += currSum - currMax
                currMax = neededTime[i]
                currSum = neededTime[i]
                prevClr = c
            else:
                currMax = max(currMax, neededTime[i])
                currSum += neededTime[i]
        return minTime + currSum - currMax