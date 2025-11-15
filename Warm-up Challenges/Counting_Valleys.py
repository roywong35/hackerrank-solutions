class Solution:
    def countingValleys(self, steps, path):
        sea_level = 0
        valley_count = 0
        for i in path:
            prev_level = sea_level
            if i == "U":
                sea_level += 1

            if i == "D":
                sea_level -= 1

            if sea_level == 0 and prev_level < 0:
                valley_count += 1
        return valley_count
    
solution = Solution()
answer = solution.countingValleys(8, "UDDDUDUU")
print(answer)

class Solution:
    def countingValleys(self, steps, path):
        sea_level = 0
        valley_count = 0

        for step in path:
            prev_level = sea_level
            if step == "U":
                sea_level += 1
            else:
                sea_level -= 1
            if sea_level == 0 and prev_level < 0:
                valley_count += 1
        return valley_count
    
solution = Solution()
answer = solution.countingValleys(8, "UDDDUDUU")
print(answer)