nums = [85, 92, 78, 95, 61, 88]

def total(scores):
    summ = 0
    for score in scores:
        summ += score
    return summ


def average(scores):
    if len(scores) == 0:
        return 0
    return round(total(scores) / len(scores), 2)


def highest(scores):
    if len(scores) == 0:
        return 0
    high = scores[0]
    for i in scores:
        if i > high:
            high = i
    return high


def count_passing(scores):
    times = 0
    for i in scores:
        if i >= 70:
            times += 1
    return times


def passing_score(nums):
    new = []
    for num in nums:
        if num >= 70:
            new.append(num)
    return new


def curve(nums, bonus):
    new = []
    for num in nums:
        if (num + bonus) > 100:
            new.append(100)
        else:
            new.append(num + bonus)
    return new


def top_three(nums):
    new = sorted(nums, reverse=True)
    return new[:3]


print(total(nums))              # 499
print(average(nums))            # 83.17
print(highest(nums))            # 95
print(count_passing(nums))      # 5
print(passing_score(nums))      # [85, 92, 78, 95, 88]
print(curve(nums, 10))          # [95, 100, 88, 100, 71, 98]
print(top_three(nums))          # [95, 92, 88]

print(highest([-5, -2, -9]))    # -2
print(average([]))              # 0
print(top_three([50, 60]))      # [60, 50]