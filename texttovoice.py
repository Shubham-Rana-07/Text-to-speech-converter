import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speak_text():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

# Create the GUI window
root = tk.Tk()
root.title("Text to Speech App")
root.geometry("400x300")
root.resizable(False, False)

# GUI Widgets
title = tk.Label(root, text="Enter text below:", font=("Arial", 14))
title.pack(pady=10)

text_input = tk.Text(root, height=8, width=40, font=("Arial", 12))
text_input.pack(pady=5)

speak_button = tk.Button(root, text="Speak", command=speak_text, font=("Arial", 12), bg="#4CAF50", fg="white")
speak_button.pack(pady=20)

# Run the app
root.mainloop()

