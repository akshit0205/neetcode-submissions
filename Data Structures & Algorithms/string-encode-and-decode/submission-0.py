class Solution:

    def encode(self, strs: List[str]) -> str:
        String=""
        for s in strs:
            String+=str(len(s))+'#'+s
        return String
    def decode(self, s: str) -> List[str]:
        i=0
        Decoded=[]
        while i < len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            word=s[j+1:j+1+length]
            Decoded.append(word)
            i=j+1+length
        return Decoded