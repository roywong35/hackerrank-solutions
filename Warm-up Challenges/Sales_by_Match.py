from collections import Counter

class Solution:
    def sockMerchant(self, n, ar):
        return  sum(count // 2 for count in Counter(ar).values())
    
solution = Solution()
answer = solution.sockMerchant(n = 9, ar = [10, 20, 20, 10, 10, 30, 50, 10, 20])
print(answer)

from collections import Counter

class Solution2:
    def sockMerchant(self, n, ar):
        count = 0
        pair = {}
        for i in ar:
            if i in pair:
                pair[i] +=1
            else:
                pair[i] = 1
            if pair[i] == 2:
                pair[i] -= 2
                count += 1
        return count
solution = Solution2()
answer = solution.sockMerchant(n = 9, ar = [10, 20, 20, 10, 10, 30, 50, 10, 20])
print(answer)