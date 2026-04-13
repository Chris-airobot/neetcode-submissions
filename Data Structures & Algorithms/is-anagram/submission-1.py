from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tmp_dict = defaultdict(int)
        for i in range(0, len(s)):
            tmp_dict[s[i]] += 1
            tmp_dict[t[i]] -= 1
        
        for element in tmp_dict:
            if tmp_dict[element] != 0:
                return False
        return True