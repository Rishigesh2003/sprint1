# def print_line():
#     print("=" * 20)


# def times_table(number):
#     for i in range(1, 11):
#         result = number * i
#         print(number, "*", i, "=", result)

# print_line()
# times_table(3)
# print_line()
# times_table(7)



def is_even(n):
    return n % 2 == 0


def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"



print(is_even(4))
print(is_even(7))


for score in [90, 80, 70, 60, 59]:
    print(letter_grade(score))
