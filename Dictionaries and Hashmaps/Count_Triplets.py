from collections import defaultdict

def countTriplets(arr, r):
    count = 0
    potential_pairs = defaultdict(int)
    potential_triplets = defaultdict(int)

    for x in arr:
        count += potential_triplets[x]

        potential_triplets[x * r] += potential_pairs[x]

        potential_pairs[x * r] += 1

    return count