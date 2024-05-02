''' 
to_str is a function that concatenates the elements of a list into a string.
eg. It returns 'car' when you give it ['c','a','r']. It takes a list as argument
and returns a string
'''
def to_str(mylist):
# n is a list of the indices of the elements in the list passed as the argument  
    n = list(range(0,len(mylist)))
# m is an integer variable which stores the index of the last element in the list passed as argument   
    m = len(mylist)-1
#string is actually a string variable formed from the concatenation of the elements of the list. It's starting character is the first character in the list
    string = mylist[0]
#this for loop iterates over the list passed as argument using the elements of n which are actually the indices of the elements in the list passed as argument
    for e in n:
        #Since string's first character is the first element in the list,we need to skip index 0
        if e <= m and e != 0: 
           #This concatenates the remaining list elements to the string
            string += mylist[e] 
           #This next if statement is not required but it is here as a caution  
            if len(string) == len(mylist):
                break
    return string 

print("WORD GUESS GAME")

'''
words is a list variable that contains all possible words to be guessed
'''
words = ['mercy','flour','impact','house','point','increase','venue','displace','gamer','motion']
indices = []

#storing the indices of the words into a list called indices
for e in words:
    indices.append(words.index(e))
  
# Importing randrange to pick an integer from a range    
from random import randrange

n = randrange(len(words))

'''
Picking a word from the list of possible words to be guessed using the randomly
generated index
'''
word = words[n]

# length is an integer variable that stores the length of the word to be guessed
length = len(word)

'''
Word is a list variable which stores the letters in the word to be guessed, as
elements of a list
'''
Word = []
'''
This for loop creates a list for the word. Eg, 'great' = ['g','r','e','a','t'].
I did this to easily compare the user's guess with the elememts of the list
It is easier to compare the guesses to the elements in the list than to directly
compare with the word itself in its string form
'''
for letter in word:
    Word.append(letter)
'''
The user's correct guesses will be stored in the Guess list. Initially,
it is made up of a number of dashes equal to the length of the word to be guessed
'''
Guess = []
n = 0 # n is a while loop variable with an initial value of 0
tries = 7 # the user is given 7 tries to guess the word

''' This while loop just sets the initial elements of the Guess list as dashes (-)
matching the length of the word. Example: If the word to be guessed is 'great'
The Guess list will be ['-','-','-','-','-']
''' 
while n < length:
    Guess.append("-")
    n += 1

# This loop runs till you ran out of tries and still haven't guessed the full word correctly
while tries != 0 and Guess != Word: 
    print(to_str(Guess)) # This prints the return value of to_str which is a string. The purpose of to_str has already being defined in this code
    letter = input("Enter a letter: ") #Taking input for a guess
    x = list(range(0,length))# x is a list of the indices of the word to be guessed
    for n in x:
        if word[n] == letter: # If guessed letter matches a letter in the word,print Correct 
            print("Correct\n")
            Guess[n] = letter
            if Guess == Word: # If all guessed letters match all actual letters
                print(f"Congrats, you guessed right. The  word is {word}")
                break
    if letter not in word:# If guessed letter doesn't match a letter in the word,print Incorrect
        print("Incorrect\n")
        tries -= 1 # Reducing tries due to a wrong guess
        print(f"{tries} tries remaining") # This prints the number of tries remaining 
if Word != Guess:
    print(f"The right word is '{word}'")
input("Game Over!!!\nPress any key to exit ")
