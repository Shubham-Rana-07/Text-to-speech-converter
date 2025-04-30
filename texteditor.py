import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename()
    if filepath:
        with open(filepath, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
        window.title(f"Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension=".txt",
                                  filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(text.get(1.0, tk.END))
        window.title(f"Text Editor - {filepath}")

# GUI window
window = tk.Tk()
window.title("Simple Text Editor")
window.geometry("600x400")

# Text area
text = tk.Text(window, wrap="word")
text.pack(expand=True, fill="both")

# Menu
menu = tk.Menu(window)
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
menu.add_cascade(label="File", menu=file_menu)
window.config(menu=menu)

# Run the app
window.mainloop()