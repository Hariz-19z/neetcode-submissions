class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        freq1={}
        freq2={}

        for ch in s:
            freq1[ch]=freq1.get(ch,0)+1

        for tu in t :
            freq2[tu]=freq2.get(tu,0)+1

        if freq1==freq2:
            return True
        else:
            return False             
        