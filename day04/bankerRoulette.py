import random
names_string = input()
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
number = random.randint(0, len(names) - 1)
selected_name = names[number]
print(f"{selected_name} is going to buy the meal today!")
