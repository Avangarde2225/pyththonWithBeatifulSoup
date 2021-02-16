def get_input_from_user():
    return input("Enter your response here ->> ")


print("Welcome to the program, what is your name?")
name_result= get_input_from_user()

print("What did you eat today?")
food_result = get_input_from_user()

print("What did you show ending did you dislike the mosdt")
show_result = get_input_from_user()

print(f"To summarize : Your name is {name_result}, you ate {food_result} food today and hated the ending of {show_result}")
