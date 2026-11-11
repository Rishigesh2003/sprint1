
for x in range(1,11):
    print(x)

for y in range(2,22,2):
    print(y)

for z in range(1,21):
    remainder = z % 2
    if remainder == 0:
        print(z)



num = int(input("Input: "))

for x in range(1,11):
    final = num * x
    print(num, "*", x, "=", final)
