class Solution:
    def jumpingOnClouds(self, c):
        step = 0
        step_count = 0
        while step < len(c)- 1:
            if step < len(c) -2 and c[step+2] == 0:
                step += 2
            else:
                step += 1
            step_count += 1
        return  step_count
    
solution = Solution()
answer = solution.jumpingOnClouds([0,1,0,0,0,1,0])
print(answer)