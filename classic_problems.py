def fizzbuzz(n):
    if n % (3*5) == 0:
        return "FizzBuzz" 
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz" 
    else:
        return str(n)


for i in range(1, 21):
    print(fizzbuzz(i))



def is_prime(n):
    if n % 2 >= 1:
        if n % 3 >= 1:
            if n % 5 >= 1:
                if n % 7 >= 1:
                    if n == 1:
                        return False
                    else:
                        return True   
                if n == 7:
                    return True
                else:
                    return False
            if n == 5:
                return True
            else:
                return False
        elif n == 3:
            return True
        else:
            return False
    elif n == 2:
        return True
    else:
        return False

def is_prime_loop(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
        
 
for n in range(1, 51):
    print(n, is_prime(n), is_prime_loop(n))

print(is_prime(121), is_prime_loop(121))






def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += (n % 10) 
        n = n // 10 
    return total
print(sum_of_digits(-1234))

