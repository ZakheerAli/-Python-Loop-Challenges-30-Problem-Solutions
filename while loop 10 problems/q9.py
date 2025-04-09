#WRITE A PROGRAM TO CHECK IF A GIVEN NUMBER ,SUCH AS 16 IS A PERFECT SQUARE

num=int(input("Enter a number = "))
i=1
is_perfect_sqaure=False
while i*i <= num:
    if i*i == num:
        is_perfect_sqaure=True
        break
    i+=1

if is_perfect_sqaure:
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not")






# num=int(input("Enter a number = "))
# i=1
# is_perfect_square=False
# while i*i <=num:
#     if(i*i==num):
#         is_perfect_square=True
#         break
#     i+=1
# if(is_perfect_square):
#     print(f"{num} is a perfect square")
# else:
#     print(f"{num} is not a perfect sqaure")