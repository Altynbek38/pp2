def permutation(s):
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            new_word = [x for x in s]
            temp = new_word[i]
            new_word[i] = new_word[j]
            new_word[j] = temp

s = str(input())
permutation(s)