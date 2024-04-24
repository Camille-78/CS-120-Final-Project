import tkinter as tk 
from tkinter import messagebox 
import random 

# List of words for the game 
words = ["python", "hangman", "programming", "coding", "challenge"]

#Italize variables 
word_to_guess = random.choice(words)
guessed_letters = []
attemps = 6 

#Create a window 
window = tk.Tk() 
window.title("Hangman Game")

#Function to check if the game is over/finished 
def is_game_over(): 
    return check_win() or check_loss() 

#Function to check is the player has won the game
    def check_loss(): 
        return attemps == 0 
    
#Function to check if the playyer has lost the game
    def check_loss():
        return attemps == 0 

#Function to handle a letter guess
    def guess_letters(): 
        global attemps 
        letter = letter_entry.get().lower() 
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
                attemps -= 1 
                update_attempts_display() 
                draw_hangman() 
                if check_loss(): 
                    messagebox.showinfo("Hangman", "You lose! (╥﹏╥) You chose the incorrect word. (｡>﹏<) The word was: " + word_to_guess)
                    reset_game()
            letter_entry.delete(0, tk.END) #Clear the input field
        else: 
            messagebox.showinfo("Hangman", "Please enter a single letter.")

    #Function to reset the game
    def reset_game(): 
        global word_to_guess, guessed_letters, attempts
        word_to_guess = random.choice(words)
        guessed_letters = []
        attemps = 6
        update_word_display()
        update_attempts_display()
        draw_hangman()

    #Function to update the word display 
    def update_word_display(): 
        display_word = ""
        for letter in word_to_guess: 
            if letter in guessed_letters: 
                display_word += letter 

            else: 
                display_word += "-"
            display_word += ""
            word_label.config(text=display_word)

    #Function to update the attempts display 
    def update_attemps_display(): 
        attemps_label.config(text=f"Attempts left: {attemps}")

    #Function to draw the hangman figure 
    def draw_hangman(): 
        canvas.delete("hangman")
        if attempts < 6: 
            canvas.create_oval(125, 125, 175, 175, width=4, tags="hangman") #Head 
        if attempts < 5: 
            canvas.create_line(150, 175, 150, 225, width=4, tags="hangman") #Body
        if attempts < 4: 
            canvas.create_line(150, 200, 125, 175, width=4, tags="hangman") #Left Arm 
        if attempts < 3: 
            canvas.create_line(150, 200, 175, 175, width=4, tags="hangman") #Right Arm
        if attempts < 2: 
            canvas.create_line(150, 225, 125, 250, width=4, tags="hangman") #Left Leg 
        if attempts < 1: 
            canvas.create_line(150, 225, 175, 250, width=4, tags="hangman") #Right Leg 

    #Create GUI elements 
    word_label = tk.Label(window, text="", font=("Times New Roman", 20))
    attempts_label = tk.label(window, text="", font=("Times New Roman", 15))
    letter_entry = tk.Entry(window, width=5, font=("Times New Roman", 15))
    guess_button = tk.Button(window, text="Guess", command=guess_letter)
    reset_button = tk.Button(window, text="Reset", command=reset_game)
    canvas = tk.Canvas(window, width=300, height=300)
    canvas.create_line(50, 250, 250, 250, width=4) #Base line 
    canvas.create_line(200, 250, 200, 100, width=4) #Post
    canvas.create_line(100, 100, 200, 100, width=4) #Beam 
    canvas.create_line(150, 100, 150, 120, width=4) #Beam 

    #Pack GUI Elements 
    word_label.pack()
    attempts_label.pack()
    letter_entry.pack()
    guess_button.pack()
    reset_button.pack() 

    #Update initial displays 
    update_word_display() 
    update_attempts_displays() 
    draw_hangman() 

    #Run the Hangman Game! 

