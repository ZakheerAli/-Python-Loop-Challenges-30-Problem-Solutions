# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.
sum=0
for i in range(1,5):
    if i % 2 == 0:
        sum+=i
print("The sum of even number  is " , sum)