import tkinter as tk
from tkinter import PhotoImage
from main_print import print_random_file

def quit_program(event=None):
    window.destroy()

def on_happy_click():
    print_random_file("Canon_iR_ADV_4025_4035_UFR_II", ['TXT1.pdf', 'TXT2.pdf', 'TXT3.pdf', 'TXT4.pdf', 'TXT5.pdf', 'TXT6.pdf', 'TXT7.pdf', 'TXT8.pdf', 'TXT9.pdf', 'TXT10.pdf', 'TXT11.pdf', 'TXT12.pdf', 'TXT13.pdf', 'TXT14.pdf', 'TXT15.pdf', 'TXT16.pdf', 'TXT17.pdf', 'TXT18.pdf', 'TXT19.pdf', 'TXT20.pdf', 'TXT21.pdf', 'TXT22.pdf', 'TXT23.pdf', 'TXT24.pdf', 'TXT25.pdf', 'TXT26.pdf', 'TXT27.pdf', 'TXT28.pdf',])
    update_icon()

def update_icon():
    pass

window = tk.Tk()
window.title("I am happy to see you")
window.configure(bg="white")
smiley_icon = PhotoImage(file="Happy.png")
emoji_label = tk.Label(window, image=smiley_icon, bg="white")
emoji_label.place(relx=0.5, rely=0.5, anchor="center")
emoji_label.bind("<Button-1>", lambda event: on_happy_click())
window.bind("<Escape>", quit_program)
window.mainloop()
