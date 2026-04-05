class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            strs.append(s[j+1:j+1+length])
            i = j + 1 + length
        return strs