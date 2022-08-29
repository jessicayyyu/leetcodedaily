def shortestSubarray(self, nums: List[int], k: int) -> int:
    N = len(nums)
    res = N+1
    prefix = [0]*(N+1)
    for i in range(N):
        prefix[i+1] = prefix[i] + nums[i]
    q = deque()
    for i in range(N+1):
        while q and prefix[q[-1]] >= prefix[i]:
            q.pop()
        while q and prefix[i] - prefix[q[0]] >= k:
            res = min(res, i - q.popleft())
        q.append(i)
    if res > N:
        return -1
    return res