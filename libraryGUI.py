import tkinter as tk
from tkinter import messagebox
import bookManager

def read_book(id):
    try:
        messagebox.showinfo("Book Search",f"{bookManager.read_book(id)}")
    except:
        messagebox.showerror("Error", "Failed to find book.")

def create_book(id, title, author, genre, year, copy_count):
    messagebox.showinfo("Book Creation",f"{bookManager.create_book(id, title, author, genre, year, copy_count)}")

# Create the main window
window = tk.Tk()
window.title("Library Manager")

window.geometry("400x200")
window.resizable(False, False)

# Create labels and entry fields
label_id = tk.Label(window, text="Book ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(window)
entry_id.grid(row=0, column=1)

label_title = tk.Label(window, text="Title:")
label_title.grid(row=1, column=0)
entry_title = tk.Entry(window)
entry_title.grid(row=1, column=1)

label_author = tk.Label(window, text="Author:")
label_author.grid(row=2, column=0)
entry_author = tk.Entry(window)
entry_author.grid(row=2, column=1)

label_genre = tk.Label(window, text="Genre:")
label_genre.grid(row=3, column=0)
entry_genre = tk.Entry(window)
entry_genre.grid(row=3, column=1)

label_copy_count = tk.Label(window, text="Copy Count:")
label_copy_count.grid(row=4, column=0)
entry_copy_count = tk.Entry(window)
entry_copy_count.grid(row=4, column=1)

label_year = tk.Label(window, text="Year:")
label_year.grid(row=5, column=0)
entry_year = tk.Entry(window)
entry_year.grid(row=5, column=1)

get_id = entry_id.get()
get_title = entry_title.get()
get_author = entry_author.get()
get_genre = entry_genre.get()
get_year = entry_year.get()
get_copy_count = entry_copy_count.get()

# Create buttons
button_add = tk.Button(window, text="Add Book", command=lambda: create_book(int(get_id), get_title, get_author, get_genre, int(get_year), int(get_copy_count)))
button_add.grid(row=6, column=0)

""" button_delete = tk.Button(window, text="Delete Book", command=)
button_delete.grid(row=6, column=1) """

""" button_update = tk.Button(window, text="Update Book", command=)
button_update.grid(row=7, column=0) """

button_search = tk.Button(window, text="Search Book (ID)", command= lambda: read_book(entry_id.get()))
button_search.grid(row=7, column=1)

# Start the main loop
window.mainloop()