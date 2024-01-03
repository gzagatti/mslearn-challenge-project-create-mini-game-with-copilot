import random

def main():
    # initialize score
    score = 0
    
    # create a dictionary to store emojis
    emojis = {
        "rock": "✊",
        "paper": "✋",
        "scissors": "✌️"
    }

    # print welcome message, be funny
    print("Welcome to Rock-Paper-Scissors!")

    # explain rules in one line
    print("Enter 'rock', 'paper', or 'scissors' to play. Enter 'quit' to exit the game.")

    # loop that runs until user enters 'quit'
    while True:

        # get user input
        user_input = input("> ")

        # set user input to lowercase
        user_input = user_input.lower()

        # resolve short forms, including quit
        if user_input == "r":
            user_input = "rock"
        elif user_input == "p":
            user_input = "paper"
        elif user_input == "s":
            user_input = "scissors"

        # if input is invalid, ask user to enter again
        if user_input not in ["rock", "paper", "scissors"]:
            print("Please enter a valid input.")
            continue

        # select a random choice for the computer
        computer_input = random.choice(["rock", "paper", "scissors"])

        # print the user input and computer input using emojis
        print(emojis[user_input], "vs", emojis[computer_input])           

        # determine the winner and compute score, print the result to the user use emojis to express emotions
        if user_input == "rock" and computer_input == "scissors":
            print("You win! 😎")
            score += 1
        elif user_input == "paper" and computer_input == "rock":
            print("You win! 😎")
            score += 1
        elif user_input == "scissors" and computer_input == "paper":
            print("You win! 😎")
            score += 1
        elif user_input == computer_input:
            print("It's a tie! 😐")
        else:
            print("You lose 😭")  

        # ask if the player wants to play again
        play_again = input("Play again? (y/n): ")

        # if user enters 'n', exit the program
        if play_again == "n":
            break

        # if user enters 'y', continue the loop
        if play_again == "y":
            continue

    # print the final score
    print("Your score is", score)

    # exit the program with goodbye message
    print("Goodbye!")
    exit()
        

if __name__ == "__main__":
    main()
