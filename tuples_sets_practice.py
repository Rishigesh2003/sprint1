def unique_count(items):
    return len(set(items))

print(unique_count(["a", "b", "a"]))


def common_skills(person1, person2):
    a = set(person1)
    b = set(person2)
    return a & b

print(common_skills(["python", "git"], ["git", "sql"]))  # {'git'}


def min_max(numbers):
    if len(numbers) == 0:
        return None, None
    return min(numbers), max(numbers)

low, high = min_max([4, 9, 1])
print(low, high)