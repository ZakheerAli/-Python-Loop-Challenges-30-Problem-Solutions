#WRITE A PROGRAM TO CHECK IF A GIVEN NUMBER IS PRIME.SUCH AS 7 IS A PRIME NUMBER

n=40
is_prime=True
for i in range(2, int(n ** 0.5)+1):
    if n % i==0:
        is_prime=False
        break


if is_prime and n > 1:
    print(n,"is a prime number")
else:
    print(n,"is not prime number")