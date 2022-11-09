secret_num = 42

guess = int(input("what is your guess?"))

if secret_num == guess:
    print("Correct")
elif secret_num -5 < guess < secret_num+5:
    print("close")
else:
    print("sorry, you're out of luck today")
