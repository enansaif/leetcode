#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        charCount = Counter(s)
        heap = []
        for char, count in charCount.items():
            heap.append((-1*count, char))
        heapq.heapify(heap)

        output = ""
        temp = []
        while heap:
            count, char = heapq.heappop(heap)
            output += char
            count += 1
            if temp:
                heapq.heappush(heap, temp.pop())
            if count < 0:
                temp.append((count, char))
        if temp:
            return ""
        return output
        
# @lc code=end

