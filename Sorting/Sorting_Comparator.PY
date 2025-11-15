from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return f"{self.name} {self.score}"
    def comparator(a, b):
        


solution = Player()
answer = solution.comparator("aabbccc")
print(answer)