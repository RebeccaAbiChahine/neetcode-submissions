class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = float("inf")
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            minNum = min(minNum, nums[mid])
            if nums[mid] >= nums[left]:
                minNum = min(minNum, nums[left])
                left = mid + 1
            else:
                right = mid - 1
        return minNum
