class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeromap = {}
        for index, num in enumerate(nums):
            if num:
                self.nonzeromap[index] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for index, num in vec.nonzeromap.items():
            if index in self.nonzeromap:
                res += num*self.nonzeromap[index]
        return res
