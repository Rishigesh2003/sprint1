num = int(input("Enter a score between 0 to 100: "))

if num >= 90 and num <= 100:
    print("A")    
    if num == 100:
        print("Perfect Score")
elif num >= 80 and num < 90:
    print("B")
elif num >= 70 and num < 80:
    print("C")
elif num >= 60 and num < 70:
    print("D")
elif num < 60 and num >= 0:
    print("F")
else:
    print("Invalid Score")