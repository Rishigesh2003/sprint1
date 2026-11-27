def word_count(text):
    words = text.split()
    return len(words)

print (f"Total Words are: {word_count("AI is the future")}")


def clean_text(text):
    word = text.strip().lower()
    return word

print(f"The cleaned text: {clean_text("  Hello WORLD  ")}")


def longest_word(text):
    names = text.split()
    length = 0
    for i in names:
        if len(i) > length:
            length = len(i)
    
    for x in names:
        if len(x) == length:
            return x
    return ""

print(f"The longest word is: {longest_word("")}")


def initials(full_name):
    name = full_name.strip().split()
    first_letter = []
    for i in name:
        first_letter.append(i[0])
    
    return "".join(first_letter).upper()


print(f"The Initials are: {initials("rishigesh rajendrakumar")}")