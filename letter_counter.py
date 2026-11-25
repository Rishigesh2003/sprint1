def count_letters(word):
    dic = {}
    
    for letter in word:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1
    return dic

def least_common(count):
    if len(count) == 0:
        return []

    mini = min(count.values())

    top = []
    for name in count:
        if count[name] == mini:
            top.append(name)
    return top[0]

print(count_letters("banana"))                     # {'b': 1, 'a': 3, 'n': 2}
print(least_common(count_letters("banana")))       # b
print(count_letters("mississippi"))                # {'m': 1, 'i': 4, 's': 4, 'p': 2}
print(least_common(count_letters("mississippi")))  # m
print(count_letters(""))                           # {}