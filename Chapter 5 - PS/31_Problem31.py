'Write a program to find unique words in a sentence.'

s = "This is a sample sentence with several words this is a test sentence"

words = s.lower().split()

unique = set(words)
print(unique)