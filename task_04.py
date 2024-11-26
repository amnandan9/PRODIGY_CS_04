import tkinter as tk
from tkinter import simpledialog, messagebox
import os

# Function to log keystrokes into a file
def log_keystrokes():
    # Ask user for input
    data = simpledialog.askstring("Keylogger Input", "Enter your keys:")
    
    if data:
        # Log the input to a file
        with open("keystrokes_log.txt", "a") as file:
            file.write(data + "\n")
        messagebox.showinfo("Keylogger", "Your input has been logged successfully!")

# Main GUI
def main():
    # Create GUI window
    root = tk.Tk()
    root.title("Keylogger Program")
    root.geometry("400x200")
    
    tk.Label(root, text="Welcome to the Keylogger Program", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Button(root, text="Log Keystrokes", command=log_keystrokes, width=20).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy, width=20).pack(pady=10)
    
    root.mainloop()

# Run the program
if __name__ == "__main__":
    main()
