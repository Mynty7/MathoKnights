import random
import tkinter as tk
from tkinter import *

#Color Constant
peach = "#ff999a"
darkblue = "#2f3b8e"
darkpurple = "#2e1b5b"

#Window
gui = tk.Tk()

#Centering the widgets
gui.grid_columnconfigure(0, weight=1)
gui.grid_columnconfigure(1, weight=1)

#Settings
gui.geometry("950x1000")
gui.title("Matho Knights Beta")
gui.resizable(False, False)
gui.configure(bg= darkpurple)
piknightimg = PhotoImage(file='Pi-Knight.png')
smallerimg = piknightimg.subsample(4, 4)

#Row and column design, R0 = Title, R1 = Pi-Knight, R2 = Question, R3 = Status, R4 = Answers, R5 = Correct/Wrong
#Menu GUI
def title():
    header = tk.Label(gui,
                  text="Matho Knights",
                  bg= darkpurple,
                  font= ("Montserrat, 30"),
                  fg = peach,
                  height=3,
                  width=15,
                  )
    header.grid(row=0, column=0, columnspan=4)
    
def back():
    back = tk.Button(gui,
                    text="Return to Level Page",
                    bg= darkpurple,
                    font= ("Montserrat, 30"),
                    fg = peach,
                    command= pagereturn,
                    )
    back.grid(row=7, column=0, columnspan=2)

def clear_screen():
    for widget in gui.winfo_children():
        widget.destroy()

def mainpage():
    clear_screen()
    title()

    global piknight 
    piknight = tk.Label(gui,
                        image=smallerimg,
                        bg=darkpurple,
                        #width=100,
                        #height=100,
                        )
    piknight.grid(row=1, column=0, columnspan=4)
    #Level Buttons
    for i in range(4):
        level_button = tk.Button(gui,
                                text=f"Level {i+1}",
                                command= level1,
                                font=("Montserrat", 30),
                                bg=darkpurple,
                                fg=peach,
                                width=10,
                                )
        level_button.grid(row=2, column=i)

def pagereturn():
    clear_screen()
    mainpage()

def gameoverpage():
    gameover_label = tk.Label(gui,
                        text= "Game Over!",
                        bg= darkblue,
                        fg= peach,
                        padx=50,
                        font=("Montserrat", 30)
                                )
    gameover_label.grid(row=3, column=0, columnspan=4)
    back()
    
def victorypage():
    gameover_label = tk.Label(gui,
                        text= "You Win!",
                        bg= darkblue,
                        fg= peach,
                        padx=50,
                        font=("Montserrat", 30)
                                )
    gameover_label.grid(row=3, column=0, columnspan=4)
    back()

def next_question():
        #pull variable from closest nested function
        global lives, num_que, status_display

        low = 0
        high = 12
        
         # Only remove old question and buttons, keep HUD and title
        for widget in gui.winfo_children():
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
                # Don't remove the title or the HUD
                if widget not in [status_display]:
                    widget.destroy()

        title()
       
        #random number generator
        num1 = random.randint(low, high)
        num2 = random.randint(low, high)

        #question generator
        que = num1 * num2
        question_show = str(f"{num1} x {num2}")

        #display question
        question_display = tk.Label(gui,
                                    text=question_show,
                                    fg=darkblue,
                                    font= ("Montserrat, 20"),
                                    bg=peach,
                                    width=20,
                                    )
        question_display.grid(row=2, column=0, columnspan=4, pady=(50, 30))

        #Creating MCQ sets
        choices = set()
        while len(choices) < 3:
            wrong_ans = random.randint(low*high, high*high)
            if wrong_ans != que:
                choices.add(wrong_ans)

        #Adding wrong_ans with correct ones to complete MCQ set
        options = list(choices) + [que]
        random.shuffle(options)                                      
        
        #Correct! or Wrong... answer display
        result_label = tk.Label(gui,
                                text="",
                                font=("Montserrat", 20,),
                                bg= darkpurple,
                                fg= peach,
                                )
        result_label.grid(row=6, column=0, columnspan=4)
        
        #answer checker
        def check_answer(selected):
            global lives, num_que

            if selected == que:
                result_label.config(text="Correct!", fg=peach)
            else:
                result_label.config(text="Wrong!", fg=peach)
                lives -= 1

            num_que += 1

            status_display.config(text=f"Lives: {lives} | Questions Left: {num_que}/10"
                                 )
            
            if lives == 0 and num_que <= 10:
                for widget in gui.winfo_children():
                    widget.destroy()
                gameoverpage()

            elif lives > 0 and num_que == 10:
                for widget in gui.winfo_children():
                    widget.destroy()
                victorypage()
                
            else: 
                #1 second interval for between each question
                gui.after(1000, next_question)
        
        #enumerate prints 1 - 4 labelling each button from 1 - 4
        for i, opt in enumerate(options):
            row = 4 + i // 2
            col = i % 2
            answer_button = tk.Button(gui,
                                    text=str(opt),
                                    font=("Montserrat", 20),
                                    width= 20,
                                    height= 5,
                                    command=lambda x=opt: check_answer(x),
                                    bg=peach,
                                    padx= 2,
                                    )
            answer_button.grid(row=row, column=col, pady=5, padx=5)

        back()

def level1():
    global lives, num_que, status_display
    clear_screen()

    lives = 5
    num_que = 0

    #status display, health & questions left
    status_display = tk.Label(gui,
                                  text=f"Lives: {lives} | Questions Left: {num_que}/10",
                                  bg=peach,
                                  fg=darkblue,
                                  font=("Montserrat", 10),
                                  width=30,
                                  height=3,
                                  )
    status_display.grid(row=3, column=0, columnspan=4)
    next_question()
    

mainpage()
    #Runs the tkinter, creates window
gui.mainloop()


