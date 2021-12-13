from collections import deque
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    q, res = deque([]), []
    for i in range(len(nums)):
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
        if i + 1 >= k:
            res.append(nums[q[0]])
        if i + 1 - k == q[0]:
            q.popleft()
    return res


