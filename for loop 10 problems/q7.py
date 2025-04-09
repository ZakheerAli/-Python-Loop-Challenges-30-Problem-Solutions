#WRITE A PROGRAM TO PRINT THE FIRST 10 TERMS OF THE FIBONACCI SEQUENCE
a=0
b=1
print( a , b , end=" ")
for _ in range(8):
    next_term = a + b
    a , b = b , next_term
    print(next_term , end=" ")