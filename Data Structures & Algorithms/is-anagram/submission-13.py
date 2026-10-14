class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = dict()
        mapT = dict()

        if len(s) != len(t):
            return False

        for i in s:
           if i in mapS:
            mapS[i] += 1
           else:
            mapS[i] = 1

        for i in t:
           if i in mapT:
            mapT[i] += 1
           else:
            mapT[i] = 1

       # for char in mapS:
         #   if char not in mapT:
         #       return False
         #   if mapS[char] != mapT[char]:
         #        return False
            

        #return True
        return mapS == mapT
                