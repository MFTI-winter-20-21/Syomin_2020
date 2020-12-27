user_name = input("Hello, what's your name?")
print("Hello", user_name)
user_old = 2020 - int(input("What year were you born?", ))
print("So you are", user_name, "and you are", user_old, "years")
if user_old < 18:
    print(user_name, "we advise you to watch a comedy")
else:
    print(user_name, "we advise you to watch a thriller")
