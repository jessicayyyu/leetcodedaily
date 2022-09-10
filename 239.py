from collections import deque
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    q = deque()
    res = [0]*(n-k+1)
    for i in range(n):
        startwindowindex = i-k+1
        while q and i-q[0] >= k:
            q.popleft()
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
        if startwindowindex >= 0:
            res[startwindowindex] = nums[q[0]]
    return res

