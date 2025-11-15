def twoStrings(s1, s2):
    word_list = set()
    for word in s1:
        word_list.add(word)
    for word in s2:
        if word in word_list:
            return "YES"
    return "NO"