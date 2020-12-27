user_name = input("Hello, what's your name?")
print("Hello", user_name)
user_old = 2020 - int(input("What year were you born?", ))
print( "Please check if the data you entered is correct: So you are", user_name, "and you are", user_old, "years?  If all okey, print '1', elif '0'")
correctness = int(input())
if correctness == 1:
    if user_old < 18:
        print(user_name, "we advise you to watch a comedy")
    else:
        print(user_name, "we advise you to watch a thriller")
else:
    print("Re-enter the data")
exit("")
