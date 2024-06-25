class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky=-1
        set_arr=set(arr)
        for i in set_arr:
            if i==arr.count(i):
                lucky=max(lucky,i)
        return lucky
        