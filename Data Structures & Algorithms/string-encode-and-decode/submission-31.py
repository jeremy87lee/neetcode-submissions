class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empty"
        string = 'é'.join(strs)
        return string
    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        
        res = []
        char_array = []
        for c in s:
            if c != 'é':
                print(c)
                char_array.append(c)
            else:
                res.append(''.join(char_array))
                char_array = []
        res.append(''.join(char_array))
        return res