class Solution:
    def GetUglyNumber_Solution(self , index: int) -> int:
        # write code here
        if index == 0:
            return 0
        factor = [2, 3, 5]
        #remove dupliicate
        mp = dict()
        #min-heap
        import heapq
        pq = []
        #1 is the first ugly number
        mp[1] = 1
        heapq.heappush(pq, 1)
        res = 0
        for i in range(index):
            res = pq[0]
            heapq.heappop(pq)
            for j in range(3):
                next = res * factor[j]
                if next not in mp:
                    mp[next] = 1
                    heapq.heappush(pq, next)
        return res

s = Solution()
s.GetUglyNumber_Solution(8)