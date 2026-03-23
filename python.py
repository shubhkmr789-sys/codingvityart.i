import random
def number_guessing_game():
lower_bound = 1
upper_bound = 100
secret_number = random.randint(lower_bound, upper_bound)
attempts = 0
print(f"Welcome to the Number Guessing Game!")
print(f"I have picked a number between {lower_bound} and {upper_bound}. Try␣
↪to guess it.")
while True:
try:
user_guess = int(input("Enter your guess: "))
attempts += 1
if user_guess < lower_bound or user_guess > upper_bound:
print(f"Please enter a number between {lower_bound} and␣
↪{upper_bound}.
")
continue
if user_guess < secret_number:
print("Too low! Try a higher number.")
elif user_guess > secret_number:
print("Too high! Try a lower number.")
else:
print(f"Congratulations! You guessed the number {secret_number}␣
↪in {attempts} attempts.")
break
except ValueError:
print("Invalid input. Please enter a whole number.")
if __name__ == "__main__":
number_guessing_game()
