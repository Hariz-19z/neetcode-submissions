class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        mydict={}

        maxi=0
        ans=0

        for num in nums:
            
            if num in mydict:
                mydict[num]+=1
            else:
                mydict[num]=1
       
            if mydict[num]>maxi:
                maxi=mydict[num]
                ans=num
        return ans

            
