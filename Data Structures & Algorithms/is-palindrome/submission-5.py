class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for c in range(len(s)):
            if s[c].isalnum():
                string.append(s[c])
        last = len(string)-1
        for i in range(0,len(string)//2,+1):
            if string[i].lower() != string[last].lower():
                print(string[i]+" "+string[last])
                return False
            last -= 1
        return True