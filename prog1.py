import random 
n = random.randint(1,100)
a = -1
guesses = 0
while (a != n):
    guesses += 1
    a = int(input("Guess The Number:"))
    if(a > 100):
        print("Invalid Guess")
        break
    if (a > n):
        print("Lower Number Please\n")
        continue
        
    elif (a < n):
        print("Higher Number Please\n")
        continue
    elif (a == n):
        print(f"\nYou have Guessed the Number {n} correctly in {guesses} attempts")  
        break