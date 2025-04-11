# игра со случайными числами
import random
number = random.randint(0, 100)
ans = None
while number != ans:
    try:
        ans = int(input("Число: "))
        if number < ans:
            print ("меньше")
        elif number > ans:
            print ("больше")
        else:
            print("вы угадали")
    except ValueError:
        print("введите целое")
