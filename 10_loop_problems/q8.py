# 8. Prime Number Checker
# Problem: Check if a number is prime.

number=11
is_prime=True
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime=False
            break
if is_prime:
    print(f"{number} is a prime")
else:
    print(f"{number} is not a prime")
