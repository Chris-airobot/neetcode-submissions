from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_output = defaultdict(list)
        for element in strs:
            string_list = [0] * 26
            for s in element:
                string_list[ord(s) - ord("a")] += 1
            final_output[tuple(string_list)].append(element)
        return list(final_output.values())

        
        