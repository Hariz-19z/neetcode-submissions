class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        seen={}

        for words in strs:
            count=[0]*26

            for ch in words:
                index=ord(ch)-ord('a')
                count[index]+=1
            key=tuple(count)

            if key not in seen:
                seen[key]=[]
            seen[key].append(words)

        return list (seen.values())


        
        