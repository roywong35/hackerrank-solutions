class Solution:
    def alternatingCharacters(self, s):
        del_count = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                del_count += 1
        return del_count

solution = Solution()
answer = solution.alternatingCharacters("AAAAA")
print(answer)

class Solution:
    def alternatingCharacters(self, s):
        del_count = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                del_count += 1
        return del_count

solution = Solution()
answer = solution.alternatingCharacters("AAAAA")
print(answer)