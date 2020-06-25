from tkinter import Tk, Label, StringVar, Entry, Listbox, Scrollbar, Button, END
import backend


def get_selected_row(event):
    global selected_tuple
    index = list_box.curselection()
    if not index:
        return
    index = index[0]
    selected_tuple = list_box.get(index)
    title_entry.delete(0, END)
    title_entry.insert(END, selected_tuple[1])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_tuple[2])
    year_entry.delete(0, END)
    year_entry.insert(END, selected_tuple[3])
    isbn_entry.delete(0, END)
    isbn_entry.insert(END, selected_tuple[4])


def view_command():
    list_box.delete(0, END)
    for row in backend.view():
        list_box.insert(END, row)


def search_command():
    list_box.delete(0, END)
    for row in backend.search(title_text.get(),
                              author_text.get(),
                              year_text.get(),
                              isbn_text.get()):
        list_box.insert(END, row)


def insert_command():
    backend.insert(title_text.get(),
                   author_text.get(),
                   year_text.get(),
                   isbn_text.get())
    view_command()


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


def update_command():
    backend.update(
        selected_tuple[0],
        title_text.get(),
        author_text.get(),
        year_text.get(),
        isbn_text.get()
    )
    view_command()


window = Tk()

window.wm_title('Bookstore')

label_title = Label(window, text='Title')
label_title.grid(row=0, column=0)

label_author = Label(window, text='Author')
label_author.grid(row=0, column=2)

label_year = Label(window, text='Year')
label_year.grid(row=1, column=0)

label_isbn = Label(window, text='ISBN')
label_isbn.grid(row=1, column=2)

title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

list_box = Listbox(window, height=8, width=35)
list_box.grid(row=2, column=0, columnspan=2, rowspan=6)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)

list_box.bind('<<lListboxSelect>>', get_selected_row)

view_all_button = Button(window, text="View all", width=12, command=view_command)
view_all_button.grid(row=2, column=3)

search_entry_button = Button(window, text="Search entry", width=12, command=search_command)
search_entry_button.grid(row=3, column=3)

add_entry_button = Button(window, text="Add entry", width=12, command=insert_command)
add_entry_button.grid(row=4, column=3)

update_entry_button = Button(window, text="Update", width=12, command=update_command)
update_entry_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)


window.mainloop()


# pyinstaller --onefile --windowed frontend.py