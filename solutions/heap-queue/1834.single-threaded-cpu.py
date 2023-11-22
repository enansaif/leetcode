#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#

# @lc code=start
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enq, prc, id) for id, (enq, prc) in enumerate(tasks)]
        tasks.sort()
        result = []
        available = []
        i, time = 0, 1
        while i < len(tasks) or available:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(available, (tasks[i][1], tasks[i][2]))
                i += 1
        
            if not available:
                time = tasks[i][0]
                continue

            processing_time, task = heapq.heappop(available)
            result.append(task)
            time += processing_time
        return result
        
# @lc code=end

