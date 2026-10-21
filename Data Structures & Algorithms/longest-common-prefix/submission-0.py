class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ans=""
        for i in range(len(strs[0])):
            ch=strs[0][i]

            for word in strs[1:]:
                if i>=len(word) or word[i]!=ch:
                    return ans 
            ans+=ch
        return ans             

    
         


