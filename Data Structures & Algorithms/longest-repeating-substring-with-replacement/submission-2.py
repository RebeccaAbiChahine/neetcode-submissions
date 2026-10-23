class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       res = 0
       charMap = {}
       left = 0
       for right in range(len(s)):
        charMap[s[right]] = 1 + charMap.get(s[right], 0)
        while (right - left + 1) - max(charMap.values()) > k:
            charMap[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
       return res