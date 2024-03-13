import time
import sys

def mind_reader():
    print("Welcome to the Mind Reader App!")
    print("Please enter a number you're thinking of:")
    user_input = input("> ")

    # Simulate scanning memories and analyzing brainwaves
    print("Scanning memories...")
    time.sleep(2)  # Pretend it's doing something important
    print("Analyzing brainwaves...")
    time.sleep(2)  # More magical processing

    # Reveal the "mind-read" number
    print(f"You're thinking of the number {user_input}!")

    # Close the app after 10 seconds
    time.sleep(10)
    sys.exit("Thank you for using the Mind Reader App. Have a magical day!")

if __name__ == "__main__":
    mind_reader()

