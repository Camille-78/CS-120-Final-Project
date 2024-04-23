import tkinter as tk

def create_new_window():
    """
    This function is designed to create the new window that will reveal the game 

    """
    new_window = tk.Toplevel()
    new_window.title("Hang Man Game")
    new_window.geometry("500x500")

    label = tk.Label(new_window, text= "Hang Man")
    label.pack(pady=20)

def only_yes_button():
    """
    Used as a way to get the user to play the game
    """
    no_button.pack_forget()
    another_open_game_button = tk.Button(root, font = ("Times", 12, "italic"), width= 20, text="Yes", bg = "darkred", fg = "lightpink", command = create_new_window)
    another_open_game_button.pack(pady = 20)


#this opens the main window 
root = tk.Tk()
root.title("Hang Man Game")
root.geometry("500x300")
root.configure(bg='lightpink')


#This labels the main window

intro_label = tk.Label(root, font=("Times", 20, "italic"), bg = "lightpink", fg = "darkred",text = "Are you ready to play ???")
intro_label.pack(pady = 20)

# This is the button to take you to the actual game

open_game_button = tk.Button(root, font = ("Times", 12, "italic"), width= 20, bg = "darkred", fg = "lightpink", text="Yes", command = create_new_window)
no_button = tk.Button(root, font = ("Times", 12, "italic"), width= 20, bg = "darkred", fg = "lightpink", text = "No", command = only_yes_button)

no_button.pack(pady = 20)
open_game_button.pack(pady = 20)


#this starts the application 
root.mainloop()

