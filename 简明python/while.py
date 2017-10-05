#!/usr/bin/python
#FileName:while.py
number = 23
running = True
while running:
    guess = int(input('enter an integer:'))
    if guess == number:
        print('congratulations,you guessed it')
        running = False
    elif guess < number:
        print('no,it is a little higher than that')
    else:
        print('no,it is a little lower than that')
else:#while中可以使用else从句
    print('the while loop is over')
print('Done')
