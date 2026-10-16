class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        result = []

        # Step 1: Count frequencies
        for num in nums:
           frequency_dict[num] = 1 + frequency_dict.get(num, 0)

        # Step 2: Create buckets
        buckets = [[] for i in range(len(nums) + 1)]

        # Step 3: Place numbers in buckets
        for num, freq in frequency_dict.items():
            buckets[freq].append(num)

        # Step 4: Retrieve k most frequent
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result