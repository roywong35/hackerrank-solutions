def minTime(machines, goal):
    low = 1
    high = min(machines) * goal

    while low < high:
        mid = (low + high) // 2

        total = 0
        for m in machines:
            total += mid // m
            if total >= goal:  # early stop optimization
                break

        if total >= goal:
            high = mid
        else:   
            low = mid + 1   # mid is definitely NOT a solution, so +1

    return low

print(minTime([2,3], 5))

def minTime(machines, goal):
    low = 1
    high = min(machines) * goal

    while low < high:
        total = 0
        mid = (low + high) // 2
        for val in machines:
            total += mid // val
            if total >= goal:
                break
        if total >= goal:
            high = mid
        else:
            low = mid + 1

    return low

print(minTime([2,3], 5))