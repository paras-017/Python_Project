


import tkinter as tk
from tkinter import messagebox
import requests


# Function to handle button click event
def search_word():
            word = entry_word.get().lower()
            url = f"https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary?word={word}"
            headers = {
                "X-RapidAPI-Key": "2cd4df8d43mshd7bad39f8f13836p1b4c15jsnad9022e874cc",
                "X-RapidAPI-Host": "dictionary-by-api-ninjas.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers)
            response_data = response.json()
            if response: messagebox.showinfo("Meaning", response_data["definition"])
            if response_data["valid"]==False: messagebox.showwarning("Word Not Found", "The word was not found in the dictionary.")



# Create the main window
window = tk.Tk()
window.title("Dictionary App")

# Create the widgets
label_word = tk.Label(window, text="Enter a word:")
label_word.pack()

entry_word = tk.Entry(window)
entry_word.pack()

button_search = tk.Button(window, text="Search", command=search_word)
button_search.pack()

# Start the main event loop
window.mainloop()