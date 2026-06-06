class Solution:

    def encode(self, strs: List[str]) -> str:
        String=""
        for s in strs:
            lenStr=str(len(s))
            String=String + "#" +str(len(lenStr))+ lenStr + s
        return String


    def decode(self, s: str) -> List[str]:
        StringList=[]
        i=0
        while i < len(s):
            if s[i] == "#":
                numOfDigits=int(s[i+1])
                length=int(s[i+2:i+2+numOfDigits])
                StringList.append(s[i+1+numOfDigits+1:i+1+numOfDigits+1+length])
            i=i+1+numOfDigits+1+length
        return StringList
