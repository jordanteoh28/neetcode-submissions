class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = True
        first_map = {}
        for first in s: 
            first_map[first] = first_map.get(first, 0) + 1

        second_map = {}
        for second in t:
            second_map[second] = second_map.get(second, 0) + 1

        return first_map == second_map