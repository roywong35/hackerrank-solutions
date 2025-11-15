class Solution:
    def repeatedString(self, s, n):
        s_count = 0
        a_count = 0
        for i in s:
            if i == "a":
                s_count +=1
        a_count = (n // len(s))*s_count
        remain = n % len(s)

        for j in range(remain):
            if s[j] == "a":
                a_count += 1
        return a_count
    
solution = Solution()
answer = solution.repeatedString("abcac", 10)
print(answer)

class Solution:
    def repeatedString(self, s, n):
        full = n // len(s)
        rem = n % len(s)
        return s.count('a') * full + s[:rem].count('a')
    
solution = Solution()
answer = solution.repeatedString("abcac", 10)
print(answer)