class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans=[]
        lucky=-1
        for i in arr:
            if i==arr.count(i) :
                ans.append(i)
                lucky=max(lucky,i)
        return lucky
        