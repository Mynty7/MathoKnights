from tkinter import *


def hello(event=None):
    print("Hello, Welcome to Matho Knight!")
    canvas.itemconfig(text, fill="grey")
    window.after(200, lambda: canvas.itemconfig(text, fill="#9961da"))


selected_level = None


def set_level(level):
    global selected_level
    selected_level = level
    print(f"Selected level : {level}")


def play_game():
    if selected_level is None:
        print(f"Please sleect a level first")
        return

    new_window = Toplevel(window)
    new_window.title(f"Matho Knight - Level {selected_level}")
    new_window.geometry("920x1000")

    Label(new_window, text=f"Welcome to level {selected_level}!", font=(
        "Super Trend", 30)).pack(pady=50)

window = Tk()

window.title("Matho Knight!")
window.geometry("920x1000")
window.config(background="white")
window.resizable(False, False)

lvl1_button = Button(window, text="LEVEL 1", font=(
    "Super Trend", 50), command=lambda: set_level(1))
# lvl1_button.place(x=70, y=375, width=160, height=90)
lvl1_button.place(relx=0.48, y=550, anchor="e", width=300, height=130)

lvl2_button = Button(window, text="LEVEL 2", font=(
    "Super Trend", 50), command=lambda: set_level(2))
lvl2_button.place(relx=0.52, y=550, anchor="w", width=300, height=130)

lvl3_button = Button(window, text="LEVEL 3", font=(
    "Super trend", 50), command=lambda: set_level(3))
lvl3_button.place(relx=0.5, y=705, anchor="center", width=300, height=130)

quit_button = Button(window, text="QUIT", font=(
    "Super Trend", 14), command=window.quit)
quit_button.place(relx=0.92, rely=0.96, width=70, height=30)

# NORMAL BUTTON
# button = Button(window, text="START")
# button.config(command = hello,
#              font=("Super Trend",
#                   20,
#                  "bold"),
#           bg="black",
#          fg="#9961da",
#         activebackground="black",
#        activeforeground="grey")
# button.pack()

# game_box = Frame(window, bg="#e6e6fa", width=900, height=250, highlightbackground="#9961da", highlightthickness=3)
# game_box.place(relx=0.5, rely=0.05, anchor="n")

# game box
game_canvas = Canvas(window, width=900, height=350,
                     bg="#fdf6ff", highlightbackground="#9961da")
game_canvas.place(relx=0.5, rely=0.05, anchor="n")
# game_canvas.create_text(450, 125, text="Battle Preview", font=("Super Trend", 30), fill="black")

# oval button
canvas = Canvas(window, width=500, height=500, bg="white")
canvas.place(relx=0.5, rely=0.12, anchor="n", width=200, height=100)
canvas.config(bg="#fdf6ff", highlightthickness=0, bd=0)

canvas_width = 950
canvas_height = 1000
center_x = canvas_width // 2
center_y = 200


# oval = canvas.create_oval(center_x - 100, center_y - 50,
#                      center_x + 100, center_y + 50,
#                     fill="black",
#                    outline="#9961da",
#                   width=3)
# text = canvas.create_text(center_x, center_y,
#                 text="START",
#                 fill="#9961da",
#                font=("Super Trend",
#                     30,
#                    "bold"))
oval = canvas.create_oval(5, 5, 195, 95, fill="black",
                          outline="#9961da", width=3)
text = canvas.create_text(100, 50, text="START",
                          fill="#9961da", font=("Super Trend", 30, "bold"))

canvas.tag_bind(oval, "<Button-1>", lambda event: play_game())
canvas.tag_bind(text, "<Button-1>", lambda event: play_game())

knight_image = PhotoImage(file="mathoknight.png").subsample(4, 4)
knight_character = Label(window, image=knight_image, bg="#fdf6ff",
                         borderwidth=0, highlightthickness=0)
knight_character.place(relx=0.80, rely=0.277, anchor="center")

tree_image = PhotoImage(file="trees.png").subsample(4, 4)
tree_label = Label(window, image=tree_image, bg="#fdf6ff",
                   borderwidth=0, highlightthickness=0)
tree_label.place(relx=0.15, rely=0.277, anchor="center")

# sky_image = PhotoImage(file="sky.png")
# sky_background = Label(window, image=sky_image,
#                      borderwidth=2)
# sky_background.place(relx=0.5, rely=0.05, anchor="n")
# sky_background.lower(canvas)

window.iconphoto(True, knight_image)

window.mainloop()
