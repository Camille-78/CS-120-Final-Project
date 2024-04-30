#both code combined to make full game
import tkinter as tk 
from tkinter import messagebox 
import random 

new_window = None

def create_new_window():
    """
    This function is designed to create the new window that will reveal the game 
    """
    global new_window
    if new_window is None or not new_window.winfo_exists():
        new_window = tk.Toplevel()
        new_window.title("Hang Man Game")
        new_window.geometry("500x600")
        new_window.configure(bg = "lightpink")
    else:
        new_window.lift()


    # Initialize game widgets so that they appear on the new window
    initialize_game_widgets()

def initialize_game_widgets():
    """ 
    Initialize widgets for the Hangman game so that it is functional for the user
    """
    global word_label, attempts_label, letter_entry, guess_button, reset_button, hints_button, canvas
    #Create GUI elements 
    word_label = tk.Label(new_window, text="", font=("Times New Roman", 20), bg = "lightpink", fg = "darkred")
    attempts_label = tk.Label(new_window, text="", font=("Times New Roman", 10), bg = "lightpink", fg = "darkred")

    letter_entry = tk.Entry(new_window, width= 15, font=("Times New Roman", 15))

    guess_button = tk.Button(new_window, font = ("Times", 12, "italic"), width= 20, bg = "darkred", fg = "lightpink", text="Guess", command=guess_letters)
    reset_button = tk.Button(new_window, font = ("Times", 12, "italic"), width= 20, bg = "darkred", fg = "lightpink", text="Reset", command=reset_game)
    hints_button = tk.Button(new_window, font = ("Times", 12, "italic"), width= 20, bg = "darkred", fg = "lightpink", text = "Hints for Failure", command = hints)

    canvas = tk.Canvas(new_window, bg = "lightpink", width=300, height=300)
    canvas.pack(pady = 40)
    canvas.create_line(50, 250, 250, 250, width=4, fill = "darkred") #Base line 
    canvas.create_line(200, 250, 200, 100, width=4, fill = "darkred") #Post
    canvas.create_line(100, 100, 200, 100, width=4, fill = "darkred") #Beam 
    canvas.create_line(150, 100, 150, 120, width=4, fill = "darkred") #Beam


    #Pack GUI Elements so that they appear for the user

    word_label.pack()
    attempts_label.pack()
    letter_entry.pack()
    guess_button.pack()
    reset_button.pack() 
    hints_button.pack()

    update_game_display()

def update_game_display():
    """ 
    Update the game display so the user knows where they stand in the game 
    """
    update_word_display()
    update_attempts_display()
    draw_hangman()


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

#after this is the code for the actual game
#dictionary of words and hints for the game 
words = {"python": "a type of snake", 
         "amazon": "a place for shopping", 
         "jellyfish": "a sea animal with tentacles", 
         "coding": "things hackers learn", 
         "challenge": "something hard", 
         "bottle": "an object that holds water", 
         "pumpkin": "you see these in the fall", 
         "honey" : "you put this in your tea when you get sick", 
         "bread" : "when making you need to kneed it", 
         "watermelon": "a red fruit", 
         "glasses": "you put these on if you can't see", 
         "snowman":"Olaf", 
         "hairspray" : "a musical about racism or a hair product",
         "dreamgirls" : "a musical about the music industry", 
         "stairs" : "after taking many flights of these you'll be winded",
         "clementine" : "a citrusy fruit",
         "confetti" : "sprayed during a celebration",
         "recognize": "a song with partynextdoor and drake"
         }

#Italize variables 
word_to_guess = random.choice(list(words.keys()))
guessed_letters = []
attempts = 6
 
def update_attempts_display():
    """
    Function to update the attempts display
    """
    global attempts
    attempts_label.config(text=f"Attempts left: {attempts}")

def is_game_over():
    """
    Function to check if the game is over/finished
    """
    return check_win() or check_loss() 

def check_win():
    """
    Function to check is the player has won the game
    """
    return all(letter in guessed_letters for letter in word_to_guess) 
    
def check_loss():
    """
    Function to check is the player has lost the game
    """
    global attempts
    return attempts == 0 


def guess_letters():
    """
    Function to handle a letter guess
    """
    global attempts, word_to_guess, guessed_letters
    letter = letter_entry.get().strip().lower() 
    if letter.isalpha() and len(letter) == 1: 
        if letter in guessed_letters: 
            messagebox.showinfo("Hangman", f"You've already guessed '{letter}'")
        elif letter in word_to_guess: 
            guessed_letters.append(letter)
            update_word_display()
            if check_win(): 
                messagebox.showinfo("Hangman", "Woohooo!! (๑ > ᴗ < ๑) Congratulations!! (づ๑•ᴗ•๑)づ♡ You win!!")
                reset_game()
        
        else: 
            guessed_letters.append(letter)
            attempts -= 1 
            update_attempts_display() 
            draw_hangman() 
            if check_loss(): 
                messagebox.showinfo("Hangman", "You lose! (╥﹏╥) You chose the incorrect word. (｡>﹏<) The word was: " + word_to_guess)
                reset_game()
        letter_entry.delete(0, tk.END) #Clear the input field
    else: 
        messagebox.showinfo("Hangman", "Please enter a single letter.")

def reset_game():
    """
    Function to reset the game
    """
    global word_to_guess, guessed_letters, attempts
    word_to_guess = random.choice(list(words.keys()))
    guessed_letters = []
    attempts = 6
    update_word_display()
    update_attempts_display()
    draw_hangman()
    hints_button.config(state=tk.NORMAL)
    hints()

def update_word_display(): 
    """
    Function to update the word display 
    """
    display_word = ""
    for letter in word_to_guess: 
        if letter in guessed_letters: 
            display_word += letter 

        else: 
            display_word += " - "
        display_word += ""
        word_label.config(text=display_word)

def draw_hangman(): 
    """
    Function drawing circles and lines to create the hangman figure
    """
    canvas.delete("hangman")
    if attempts < 6: 
        canvas.create_oval(125, 125, 175, 175, width=4, tags="hangman", outline = "white") #Head 
    if attempts < 5: 
        canvas.create_line(150, 175, 150, 225, width=4, tags="hangman", fill = "white") #Body
    if attempts < 4: 
        canvas.create_line(150, 200, 125, 175, width=4, tags="hangman", fill = "white") #Left Arm 
    if attempts < 3: 
        canvas.create_line(150, 200, 175, 175, width=4, tags="hangman", fill = "white") #Right Arm
    if attempts < 2: 
        canvas.create_line(150, 225, 125, 250, width=4, tags="hangman", fill = "white") #Left Leg 
    if attempts < 1: 
        canvas.create_line(150, 225, 175, 250, width=4, tags="hangman", fill = "white") #Right Leg 


def hints():
    """
    A function that gives hints to the user once they guess
    """
    global attempts
    if attempts < 6:
        hint = words[word_to_guess]
        messagebox.showinfo("Hint", hint)
        hints_button.config(state=tk.DISABLED)
    else:
        None

#this starts the application 
root.mainloop()
