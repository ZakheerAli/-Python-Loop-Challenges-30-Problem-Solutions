#WRITE A PROGRAM TO CALCULATES THE FACTORIAL OF A GIVEN NUMBERS SUCH AS 5

n=10
fact=1
for i in range(1 , n+1):
    fact*=i
print(fact)