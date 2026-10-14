class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        solution = []
        for i in range (0, len(nums)):
            current = nums[i]
            sub = target - current 
            if sub in hashmap:
                solution.append(hashmap[sub])
                solution.append(i)
                return solution
            else:
                hashmap[current] = i

        return solution
