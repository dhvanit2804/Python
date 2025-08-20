'''Write a program to create a dictionary of Hindi words with values as their English 
translation. Provide user with an option to look it up!'''

words = {
    "Dost" : "Friend",
    "Billi" : "Cat",
    "Khana" : "Food",
    "Pyaar" : "Love"
}

word = input("Enter the word you want meaning of: ")
print(words[word])