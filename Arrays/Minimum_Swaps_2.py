class Solution:
    def minimumSwaps(self, arr):
        count = 0
        i = 0
        while i < len(arr):
            if arr[i] != i + 1:
                correct_index = arr[i] - 1
                arr[i], arr[correct_index] = arr[correct_index], arr[i]
                count += 1
            else:
                i += 1
        return count

solution = Solution()
answer = solution.minimumSwaps([7,1,3,2,4,5,6])
print(answer)