def cleanup(text):
    word = text.replace("!", "").replace(",","").replace(".","").replace("?","")
    return word.lower().split()
    
def words(text):
    return len(text)

def unique(text):
    return set(text)

def count_words(text):
    if len(text) == 0:
        return "", 0

    counts = {}

    for i in text:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    counted = 0
    for x in counts:
        if counts[x] > counted:
            counted =  counts[x]

    for words in counts:
        if counts[words] == counted:
            return words, counted

def longest(text):
    lenght = 0

    for i in text:
        if len(i) > lenght:
            lenght = len(i)
    
    for x in text:
        if len(x) == lenght:
            return x
    
def average(text):
        word_num = len(text)
        letters = 0

        for i in text:
            letters += len(i)
        return letters / word_num

def once(text):
    counts = {}

    for i in text:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    once_only = []
    for x in text:
        if counts[x] == 1:
            once_only.append(x)
    
    return ", ".join(once_only)


def main(text):
    cleaned = cleanup(text)
    if cleaned == []:
        print("Invalid, Try again")
    else:
        print()
        print("=== Text Analysis===")
        print(f"Words: {words(cleaned)}")
        print(f"Unique words: {len((unique(cleaned)))}")
        word, count = count_words(cleaned)
        print(f"Most common: {word} ({count} times)" )
        print(f"Longest word: {longest(cleaned)}")
        print(f"Average word length: {average(cleaned):.1f}")
        print(f"Words used once: {once(cleaned)}")
        print()


main(input("Paste your text: "))