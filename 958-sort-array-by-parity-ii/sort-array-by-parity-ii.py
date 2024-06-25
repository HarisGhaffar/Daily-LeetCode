class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        ans=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            elif i%2!=0:
                odd.append(i)
        
        for i in range(len(odd)):
            ans.append(even[i])
            ans.append(odd[i])
        return ans

        