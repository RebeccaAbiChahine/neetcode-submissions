class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]
            if target < currentSum:
                 right -= 1
            elif target > currentSum:
                 left += 1
            else:
                 return [left + 1, right + 1]

        return []

           


        