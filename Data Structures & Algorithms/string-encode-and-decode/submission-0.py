class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string=""

        for s in strs:
            for ch in s:
                encoded_string+=chr(ord(ch)+5)
            encoded_string+='_'

        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_str_list=[]
        temp = s.split("_")
        temp.pop()

        for st in temp:
            word=""
            for ch in st:
                word += chr(ord(ch)-5)
            decoded_str_list.append(word)

        return decoded_str_list

