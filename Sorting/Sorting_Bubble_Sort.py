def countSwaps(a):
    swap_count = 0
    
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap_count += 1
    
    first = a[0]
    last = a[-1]
                
    print(f"Array is sorted in {swap_count} swaps.")
    print(f"First Element: {first}")
    print(f"Last Element: {last}")