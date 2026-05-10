class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = set(nums)
        return len(answer) != len(nums)        
        