#WRITE A PROGRAM TO COUNT OCCURENCES OF EACH CHARACTER IN THE WORD PROGRAMMING
word="programming"
dictionary={}
for i in word:
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i]=1

# print(dictionary)
for i,count in dictionary.items():
    print(i ,":",count)