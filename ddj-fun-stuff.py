
#I want the results to be displayed

import tkinter as tk
from tkinter import messagebox

print("Hello there!\nAsk me question on the Dao?\nI can show you some videos too.")

def search():
    # Retrieve the search query from the user
    query = search_entry.get()

    # Check if the query matches the expected question
    if query.lower() == "who founded dao":
        # Show the link in a messagebox
        messagebox.showinfo("Search Result", "You can learn more about Daoist thought at this link:\nhttps://en.daoinfo.org/wiki/Daoist_thought_prior_to_Qin_dynasty_(pre-221_BC)")
    else:
        # If the query is not found, display an error message
        messagebox.showerror("No Results", "Sorry, no results found for your query.")

# Create the main window
window = tk.Tk()
window.title("Daoism Search")

# Create a label for the search bar
label = tk.Label(window, text="Enter your query:")
label.pack(pady=10)

# Create a search entry box
search_entry = tk.Entry(window, width=50)
search_entry.pack(pady=10)

# Create a search button that triggers the search function
search_button = tk.Button(window, text="Search", command=search)
search_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()


   

