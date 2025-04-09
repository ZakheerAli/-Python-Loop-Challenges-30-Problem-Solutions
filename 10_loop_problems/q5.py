# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.
word="teeteir"
for char in word:
    if word.count(char) == 1:
        print("First non repeated character in a string is ",char)
        break