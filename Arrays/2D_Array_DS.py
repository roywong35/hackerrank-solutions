class Solution:
    def hourglassSum(self, arr):
        max_sum = -float("inf")
        for i in range(4):
            for j in range(4):
                sum_1 = arr[i][j]+arr[i][j+1]+arr[i][j+2]
                sum_2 = arr[i+1][j+1]
                sum_3 = arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                curr_sum = sum_1 + sum_2 + sum_3
                max_sum = max(max_sum, curr_sum)
        return max_sum
    
solution = Solution()
answer = solution.hourglassSum(arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
])
print(answer)