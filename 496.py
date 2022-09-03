def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hashmap, stack = {}, []
    for i in range(len(nums2)-1, -1, -1):
        while stack and nums2[i] >= stack[-1]:
            stack.pop()
        if not stack:
            hashmap[nums2[i]] = -1
        else:
            hashmap[nums2[i]] = stack[-1]
        stack.append(nums2[i])
    res = [0] * len(nums1)
    for i in range(len(nums1)):
        res[i] = hashmap[nums1[i]]
    return res