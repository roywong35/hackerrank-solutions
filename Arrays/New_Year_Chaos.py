class Solution:
    def minimumBribes(self, q):
        bribes = 0
        for i in range(len(q)):
            # Check if anyone moved more than 2 spots ahead
            if q[i] - (i + 1) > 2:
                print("Too chaotic")
                return
            
            # Count how many people ahead of q[i] originally are now behind q[i]
            # (start from one position before q[i]'s original spot or 0)
            for j in range(max(0, q[i] - 2), i):
                if q[j] > q[i]:
                    bribes += 1
                    
        print(bribes)
solution = Solution()
answer = solution.minimumBribes([1, 3, 2, 4, 5])

class Solution2:
    def minimumBribes(self, q):
        bribes = 0
        for i in range(len(q)):
            if q[i] - 1 - 2 > i:
                print("Too chaotic")
                return
            for j in range(max(0, q[i]-2), i):
                if q[j] > q[i]:
                    bribes += 1            
        print(bribes)
solution = Solution2()
answer = solution.minimumBribes([1, 3, 2, 4, 5])
