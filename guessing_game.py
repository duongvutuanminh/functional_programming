from random import randint
num = randint(1,100)
res = False
count = []
first_time = 0
while res == False:
    first_time += 1
    user = input("Guess a number: ")
    user = int(user)
    count.append(user)
    if user == num:
        print("Found it!")
        print(f"The answer is: {num}, you have guessed {len(count)} time(s):{count}")
        res = True
    elif abs(user-num)<10 and first_time == 1:
        print("Near")
        continue
    elif abs(user-num)>=10 and first_time == 1:
        print("Far")
        continue
    elif abs(num - count[-2]) < abs(num-user):
        print("Farer")
    elif abs(num - count[-2]) > abs(num-user):
        print("Nearer! Come on")
    elif user == count[-2]:
        print("Pick a number different from the last time!!!")
