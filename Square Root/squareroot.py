n = n = float(input("enter a number:"))
guess = n/2
while (guess*guess > n):
    guess = guess -0.00000000000001
print("square root:",guess)