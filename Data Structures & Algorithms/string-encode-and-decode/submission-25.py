class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return("empty")
        string = 'é'.join(strs)
        print(string)
        return string
    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        array = []
        char_array = []
        for c in s:
            if c == 'é':
                string = "".join(char_array)
                array.append(string)
                char_array = []
            else:
                char_array.append(c)
        if s != []:
            string = "".join(char_array)
            array.append(string)
        return array