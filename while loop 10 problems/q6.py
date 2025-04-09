#WRITE A PROGRAM TO COUNT THE NUMBERS OF CONSONENTS IN THE WORLD "LEARNING"
word=input("Enter a word to check= ")
vowels="aeiou"
count=0
idx=0

while idx < len(word):
    if word[idx].lower() not in vowels and word[idx].isalpha():
        count+=1
    idx+=1

print(f"Number of consonants in {word} = {count}")