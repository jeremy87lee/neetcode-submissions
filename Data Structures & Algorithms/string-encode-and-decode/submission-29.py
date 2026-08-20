class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empty"
        new_str = 'é'.join(strs)
        return new_str
    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        char_array = []
        array = []
        for c in s:
            if c == 'é':
                string = ''.join(char_array)
                array.append(string)
                char_array = []
            else:
                char_array.append(c)
        if s != "empty":
            string = ''.join(char_array)
            array.append(string)
        return array