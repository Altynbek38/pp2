def get_permutation(s, k = 0):
    if k == len(s):
        print("".join(s))

    for i in range(k, len(s)):
        new_word = [j for j in s]
        print(new_word)
        temp = new_word[k]
        new_word[k] = new_word[i]
        new_word[i] = temp
        get_permutation(new_word, k + 1)


s = str(input())
print(get_permutation(s))

#abc    bac     cba
#acb    bca     cab