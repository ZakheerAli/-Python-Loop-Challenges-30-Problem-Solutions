#WRITE A PROGRAM TO PRINT THE WORD "PYTHON" IN REVERSE USING A FOR LOOP
# way 1
word="Zakheer Ali"
for i in range(len(word)-1,-1 , -1):
    print(word[i] ,end=" ")
 
# Way 2     
string="zakheer ali"
reversed_str=""
for char in string:
    reversed_str=char + reversed_str
print(reversed_str)