from collections import defaultdict
class Solution:
    def freqQuery(self, queries):
        freq = defaultdict(int) 
        freqCount = defaultdict(int)
        result = []

        for op, val in queries:
            if op == 1:
                old = freq[val]
                new = old + 1
                freq[val] = new
                if old > 0:
                    freqCount[old] -= 1
                freqCount[new] += 1

            elif op == 2:
                old = freq[val]
                if old > 0:
                    freqCount[old] -= 1
                    new = old - 1
                    freq[val] = new
                    if new > 0:
                        freqCount[new] += 1

            elif op == 3:
                result.append(1 if freqCount[val] > 0 else 0)

        return result
solution = Solution()
answer = solution.freqQuery(queries = [
    [1, 5],
    [1, 6],
    [3, 2],
    [1, 10],
    [1, 10],
    [1, 6],
    [2, 5],
    [3, 2]
])
print(answer)