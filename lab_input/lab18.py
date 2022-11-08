def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter your name:")

    # display the input back to the user.
    print("You told me the name is is: " + user_input)
    
    day = input("what day of the week is it?")
    print("the day of the week is:",day)

    print("Hello, " + user_input + "!" + " Happy " +day+"!");
    print(f"Hello, {user_input}! Happy {day}!")
# this calls main
main()
