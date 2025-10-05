import random
import tkinter as tk
#Tkinter GUI
gui = tk.Tk()
gui.geometry("1920x1080")
gui.title("Matho Knights Beta")
gui.resizable(False, False)

def menu():
    print("/ ***************************************  \ \n| *************************************** |\n| ******* Welcome to Matho Knights beta version ******* |\n| *******    Select your Level!   ******* |\n| *************************************** |")
    print("| Levels | [1]Easy | [2]Medium | [3]Hard  |")
    level_selector = int(input("|               Select Your Level! :"))

    match level_selector:

        case 1:
            print("|        Preparing level 1....        |")
            level1()

def level1():
    #Declare variables
    low = 0
    high = 12
    lives = 5
    num_que = 0
    
    while lives > 0 and num_que < 10: 

        #random number generator
        num1 = random.randint(low, high)
        num2 = random.randint(low, high)

        #question generator + display
        que = num1 * num2
        print(f"|             {num1} x {num2} = ?              |")
        print("|         Available Answers:          |")

        #Creating MCQ sets
        choices = set()
        while len(choices) < 3:
            wrong_ans = random.randint(low*high, high*high)
            if wrong_ans != que:
                choices.add(wrong_ans)

        #Adding wrong_ans with correct ones to complete MCQ set
        options = list(choices) + [que]
        random.shuffle(options)

        #printing all MCQ options, enumerate converts the answers into a label from 1-4, so if 1 = 24, when inputted 1 it actually means 24
        for x, opt in enumerate (options, 1):
            print(f"[{x}] {opt}")

        #user's answer from [1-4] answers
        answer = int(input("Answer = "))
        
        #answer checker
        if options[answer - 1] == que:
            num_que += 1
            print(f"| correct! | Lives: {lives} | Questions Left: {num_que}/10 |")
                
        elif options[answer - 1] != que:
            lives -= 1
            num_que += 1
            print(f"| incorrect! | lives: {lives} | Questions Left: {num_que}/10 |")

        else:
            print("you have died...")
            break

menu()

gui.mainloop()


