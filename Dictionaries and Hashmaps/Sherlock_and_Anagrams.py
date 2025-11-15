def sherlockAndAnagrams(s):
    substr_count = {}

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = ''.join(sorted(s[i:j]))
            substr_count[substring] = substr_count.get(substring, 0) + 1

    total = 0
    for count in substr_count.values():
        if count > 1:
            total += count * (count - 1) // 2

    return total