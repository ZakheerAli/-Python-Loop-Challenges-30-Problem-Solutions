#WRITE A PROGRAM TO REVRESE EACH WORD IN THE SENTENCE "HELLO WORLD" USING A WHILE LOOP
sentence="hello world"
words=sentence.split()
for word in words:
    i=len(word)-1
    while i >= 0:
        print(word[i] ,end="")
        i-=1
    print( end=" ")