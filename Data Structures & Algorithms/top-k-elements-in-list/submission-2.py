class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
            
        result = []
        for key, value in sorted(freq_dict.items(), key = lambda x: x[1], reverse = True):
            result.append(key)
            if len(result) == k:
                break
        return result