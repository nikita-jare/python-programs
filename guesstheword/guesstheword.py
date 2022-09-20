import random

dataset = open("./dataset/word_list.txt", "r")
words = dataset.readlines()
#words = ['kindly', 'recite', 'repeat', 'tree', 'display', 'geeks', 'coder', 'programmer', 'python', 'premium', 'watch','television']
word = random.choice(words)
word = word.strip().lower()
#print(word)
indexes = random.sample(range(0,len(word)), 2)
guesses = ''   #Letters user has already guessed

for i in indexes:
    guesses += word[i]
    
chances = len(word) + 3 #Number of chance to guess the whole word
name = input("Enter your name:")

print(f"Welcome {name}!")
print(f"All the best :) You have total {chances} chances to guess the whole word")

while chances > 0:   
    won = True
    for ch in word:
        if ch in guesses:
            print(ch, end=" ")
        else:
            print("_",end=" ")
            won = False
            
    if won == True:
        print("\n\nYou won!")
        print(f"Your score is {chances*10}")
        break
        
    guess = input("\nGuess the letter in the word:") #accept user input
    guesses += guess
    
    if guess not in word:
        chances -= 1
        print("\nWrong guess.")
        print(f"You have {chances} left.\n")
        
    if chances == 0:
        print("\n\nYou lost!")
        print("Better luck next time")
        print(f"The word was: {word}")
