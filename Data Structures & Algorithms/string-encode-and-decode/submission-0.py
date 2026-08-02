class Solution:

    def encode(self, strs: List[str]) -> str:
        original_str = ""

        print(strs)
        for i in range(0, len(strs)) :
            original_str += str(len(strs[i])) + "*" + strs[i]

        return original_str

    def decode(self, s: str) -> List[str]:
        list_str = []
        i = 0
        while i < len(s):
            pos_star = s.find("*", i)
            length_word = int(s[i:pos_star])
            list_str.append(s[pos_star+1:length_word + pos_star + 1])
            i = pos_star + length_word + 1

        return list_str