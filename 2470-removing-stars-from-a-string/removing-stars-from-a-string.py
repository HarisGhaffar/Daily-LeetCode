class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for star in s:
            if star=='*':
                stack.pop()
            else:
                stack.append(star)
        
        return "".join(stack)
        
        