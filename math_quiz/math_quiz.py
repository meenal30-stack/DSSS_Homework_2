import random

# Function to get random number from given range 
def Number(min, max):
    """
    Purpose: Generates random integer from the defined minimum and maximum range
    --------
    Parameters:
        min - int
            minimum value for random integer
        max - int
            maximum range for random integer
    --------
    Return: Integer between min and max range
    """
    return random.randint(min, int(max)) # Ensure max is conveted to integer

# Function to get random operator from provided choices
def Operator():
    """
    Purpose: Generates random operator for arithmetic application
    --------
    Parameters: None
    --------
    Return: String choosing between provided operator set [ + addition, - substraction or * multiplication ]
    """
    return random.choice(['+', '-', '*']) # Selection between addition, substraction or multiplication operator


# Function to add, subtract, multiply the numbers based on requirement
def Operation(n1, n2, o):
    """
    Purpose: Generates operations based on operator on the numbers and returns answer
    --------
    Parameters: 
        n1 - int
            Number 1 for operation
        n2 - int
            Number 2 for operation
        o - String
            Operator for arithmetic operations
    --------
    Return: 
        Tuple containing problem as string
        Integer containg answer
    """
    p = f"{n1} {o} {n2}" # Print the math problem for user
    if o == '+': a = n1 + n2 # Addition operator implementation
    elif o == '-': a = n1 - n2 # Substraction operator implemention
    else: a = n1 * n2 # Multiplication operator implementation
    return p, a # Returns problem and answer

# Function to take inputs from user, call other functions according to requirement and calculate score basd on user input
def math_quest():
    """
    Generates a math quiz game, presenting the user with math problems, taking user inputs and tracking the score based on user provided answers.

    The game generates random math problems, prompts the user for an answer, and evaluates
    if the answer is correct. At the end, it displays the user's final score.
    """
    user_score = 0 # Initial user score
    total_score = 3 # Total score

    # Quiz Instructions
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop for total number of questions
    for _ in range(total_score):
        
        n1 = Number(1, 10); # Range for number 1
        n2 = Number(1, 5.5); # Range for number 2
        o = Operator() # Operator selection

        PROBLEM, ANSWER = Operation(n1, n2, o) # Returns problem and answer
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ") # User input
        try:
                useranswer = int(useranswer) # Ensure input is integer
                # Checks if the user input matches with the answer
                if useranswer == ANSWER:
                    print("Correct! You earned a point.")
                    user_score += -(-1) # Updating user score
                else:
                    print(f"Wrong answer. The correct answer is {ANSWER}.") # No points for wrong answer
                
        except ValueError:
                print("Invalid input. Please enter a valid integer as answer. Please start the quiz again")
                return math_quest()


    print(f"\nGame over! Your score is: {user_score}/{total_score}") # Final score display

# Run the math quest game if the script is executed directly
if __name__ == "__main__":
    math_quest()