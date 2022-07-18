#!/usr/bin/env python
# coding: utf-8

# In[6]:


#importing necessary packages
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


#set up main window
root = Tk()
root.title("Notes - Untitled")
root.geometry("400x650")
#prevent users from resizing window, both horizontally and vertically
root.resizable(False, False)


#initialize note_status
note_status = False


#functions

#functions to change all widget button's backgrounds when user hovers over it and leaves it
def enter_button(e):
    e.widget.config(background = "#D4D4D4")
#SystemButtonFace is default colour

def leave_button(e):
    e.widget.config(background = "SystemButtonFace")
    

#functions in top_frame                                              
#clear text in text-box
def clear():
    #delete all text from text_box
    text_box.delete(1.0,END)

def bold_it():

    try: 
        #create font
        bold_font = font.Font(text_box, text_box.cget("font"))
        bold_font.configure(weight = "bold")
    
        #creating tag called "bold" which bolds text upon condition
        text_box.tag_configure("bold", font = bold_font)
    
        #creating a bold tag which highlights first character
        bold_tag = text_box.tag_names("sel.first")
    
        #condition for checking to see if tag is applied or not in the first highlighted character
        #if tag is applied, remove the bold from first-highlighted text and vice-versa
        #-last highlighted text
        #"bold" needs to be matched in the tag
        if "bold" in bold_tag:
            text_box.tag_remove("bold","sel.first","sel.last")
        else:
            text_box.tag_add("bold","sel.first", "sel.last")
    
    #don't raise exception if user attempts to press bold button with no text in text-box
    except TclError: 
        pass

def italics_it():
    
    try:
        #create a font
        italics_font = font.Font(text_box, text_box.cget("font"))
        italics_font.configure(slant = "italic")
    
        #create a tag called "italic"
        text_box.tag_configure("italics", font = italics_font)
    
        italics_tag = text_box.tag_names("sel.first")
    
        #condition to see whether tag has been applied or not
        if "italics" in italics_tag:
            text_box.tag_remove("italics", "sel.first","sel.last")
        
        else: 
            text_box.tag_add("italics", "sel.first", "sel.last")
        
    #don't raise exception if user attempts to press bold button with no text in text-box
    except TclError: 
        pass

    
#file functions
def save_note(): 
        
    #check if existing, previously saved file is opened
    
    if note_status: 
        
        with open(note_status, "w") as f: 
            
            f.write(text_box.get(1.0, END))
            
        messagebox.showinfo("File Pop-Up", "File Saved!")
            
    # if file has not existed before
    # performing save_as to an untitled note
    else: 
        #call save_as function
        save_as_note()

def save_as_note():
    #save as "all files" option
    saved_note = filedialog.asksaveasfilename(initialdir="/", title = "Save File As", filetypes = [("All Files","*.*")])

    #address condition of if "save file" is pressed: 
    
    if saved_note:
        
        global note_status
        note_status = saved_note
         
        root.title(saved_note.replace("C:/Users/safwa/OneDrive/Desktop/Notes_Application/","Notes - "))
        
        with open(saved_note, "w") as f: 
            
            f.write(text_box.get(1.0, END))
            
        messagebox.showinfo("File Saved Pop-Up","Your file was saved to a directory!")
      
    else: 
        pass
        

def open_note(): 
    
    #accept txt files + all files
    opened_note = filedialog.askopenfilename(initialdir="/", title = "Select File", filetypes = [("All Files","*.*")])
    
    #address condition of opening a file
    if opened_note: 
        
        #set-aside variable name and globalize it (so can use it)
        global note_status
        note_status = opened_note
        
        root.title(opened_note.replace("C:/Users/safwa/OneDrive/Desktop/Notes_Application/","Notes - "))
        
        #read-mode of file
        with open(opened_note, "r") as f: 
        
        #grab content from file
            content = f.read()
            
        #delete the exisitng content in text box
        text_box.delete(1.0, END)

        #now insert the content from existing file into text box
        text_box.insert(END, content)
    
    #raise no exception if cancel is pressed in filedialog
    else: 
        pass
    
    
def new_note(): 
    
    #delete all content in text_box
    text_box.delete(1.0,END)
    root.title("Notes - Untitled")
    
    
#frames
top_frame = LabelFrame(root, padx = 36, pady = 10)
button_frame = LabelFrame(root, padx = 30, pady = 10)
text_frame = LabelFrame(root, padx = 10, pady = 10)
bottom_frame = LabelFrame(root, borderwidth = 0, highlightthickness = 5)

top_frame.grid(row = 0 , column = 0)
button_frame.grid(row = 1, column = 0, pady = 10)
text_frame.grid(row = 2, column = 0, pady = 1)
bottom_frame.grid(row = 3, column = 0, pady = 3)

#top_frame content
#padx increases distance between buttons
Notes_label = Label(top_frame, text = "Notes", fg = "black", font = 1, padx = 141)
Notes_label.grid(row = 0, column = 0)


#button_frame content
#bold button
bold_button = Button(button_frame, text = "B", padx = 4, pady = 2, command = bold_it)
bold_button.grid(row = 0, column = 0)

#italicsize button
italics_button = Button(button_frame, text = "I", padx = 4, pady = 2, command = italics_it)
italics_button.grid(row = 0, column = 2, padx = 15)

clear_button = Button(button_frame, text = "Clear", padx = 4, pady = 2, command = clear)
clear_button.grid(row = 0, column = 3)

#textframe content
text_box = Text(text_frame, width = 46, height = 27)
text_box.grid(row = 0, column = 0)

main_scrollbar = ttk.Scrollbar(text_frame, orient = "vertical", command = text_box.yview)
main_scrollbar.grid(row = 0, column = 1, sticky = NS)
text_box["yscrollcommand"] = main_scrollbar.set


#bottom frame content
save_button = Button(bottom_frame, text = "Save Note", padx = 2, pady = 2, command = save_note)
save_button.grid(row = 0, column = 0, padx = 10, pady = 10)

save_as_button = Button(bottom_frame, text = "Save Note as", padx = 2, pady = 2, command = save_as_note)
save_as_button.grid(row = 0 , column = 1, padx = 15, pady = 10)

open_button = Button(bottom_frame, text = "Open Note", padx = 2, pady = 2, command = open_note)
open_button.grid(row = 0, column = 2, padx = 15, pady = 10)

new_note_button = Button(bottom_frame, text = "New Note", padx = 2, pady = 2, command = new_note)
new_note_button.grid(row = 0 , column = 3, padx = 15, pady = 10)


#binding all buttons for changing colours when user hovers over it and leaves it
bold_button.bind("<Enter>", enter_button)
bold_button.bind("<Leave>", leave_button)
italics_button.bind("<Enter>", enter_button)
italics_button.bind("<Leave>", leave_button)
clear_button.bind("<Enter>", enter_button)
clear_button.bind("<Leave>", leave_button)
save_button.bind("<Enter>", enter_button)
save_button.bind("<Leave>", leave_button)
save_as_button.bind("<Enter>", enter_button)
save_as_button.bind("<Leave>", leave_button)
open_button.bind("<Enter>", enter_button)
open_button.bind("<Leave>", leave_button)
new_note_button.bind("<Enter>", enter_button)
new_note_button.bind("<Leave>", leave_button)


# main program loop
root.mainloop()


# In[ ]:




