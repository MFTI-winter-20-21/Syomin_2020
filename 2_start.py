user_name = input("Hello, what's your name?")
print("Hello", user_name)
user_old = 2020 - int(input("What year were you born?", ))
if 4 <= user_old >= 130:
    exit(" Are u a dino or an alien?")
if user_old < 18:
    print("Sorry, but u aren't allowed to be on this site")
else:
    country = input("Where are u from?")
