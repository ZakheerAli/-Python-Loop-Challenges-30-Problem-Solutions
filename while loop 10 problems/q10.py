#WRITE A PROGRAM TO COUNT THE OCCURENCES OF CHARACTER "S" IN THE STRING "SUCCESS"
word=input("Enter a word = ")
char_to_count=input("Enter a character to count = ")
idx=0
count=0
while idx < len(word):
    if word[idx].lower() in char_to_count and word[idx].isalpha():
        count+=1
    idx+=1

print(f"The number of {char_to_count} in {word}= {count}")