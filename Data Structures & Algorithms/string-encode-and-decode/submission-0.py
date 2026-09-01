class Solution:

    def encode(self, strs: List[str]) -> str:

        encode = ""

        for string in strs:
            encode += str(len(string)) + "|" + string

        return encode


    def decode(self, s: str) -> List[str]:

        i = 0
        j = 0
        decode =[]

        while i < len(s):

            while s[j] != "|":
                j+=1

            length = int(s[i:j])
            word = s[j+1 : j + 1 + length]
            decode.append(word)

            i = j + 1 + length
            j = i

        return decode

