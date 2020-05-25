from tkinter import *

#Creating an app window
app = Tk()




#Creating the add_item function
def add_item():
    pass

app.title("HackerBox")
app.geometry('700x350')

#Label and Entry for the name
name_text = StringVar()
#creating a label, a label can display text, archor or image
name_label = Label(app, text = "Hacker name", font =  14, pady = 10) 
#a grid helps to place the label inside the window
name_label.grid(column = 0, row = 0 )
#Creating an entry, for text input
name_entry = Entry(app, textvariable = name_text, justify = CENTER, width = 30)
name_entry.grid(row = 0, column = 1, sticky = E, padx = 10)

#Label and entry for the workplace
workplace_name = StringVar()
workplace_label = Label(app, text = "Current Workplace", font = 14, pady = 10)
workplace_label.grid(row = 0, column = 2)
workplace_entry = Entry(app, textvariable= workplace_name, justify = CENTER, width = 30)
workplace_entry.grid(row = 0, column = 3, sticky = E, padx = 10)

#Label and entry for age
age_input = StringVar()
age_label = Label(app, text = "Age", font = 14 , pady = 10)
age_label.grid(row = 1, column = 0)
age_entry = Entry(app, textvariable = age_input, justify = CENTER, width = 30)
age_entry.grid(column = 1, row = 1, sticky = E)

#Creating a dropdown list for level
OptionList = ['Choose an option','Beginner','Intermediate', 'Advanced']
level_input = StringVar()
level_input.set(OptionList[0])
level_opt = OptionMenu(app, level_input, *OptionList)
level_opt.config(width= 13, font = 11 )
level_opt.grid(column = 3, row = 1, sticky = E, padx = 10)
level_label = Label(app, text = "Level Options", font = 14, pady =10)
level_label.grid( row =1, column = 2)


#Creating a list box 
HackerBox = Listbox(app, height = 8, width = 50)
HackerBox.grid(row =3, column = 0, columnspan = 3, rowspan = 6, pady = 20, padx = 20)

#Creating a scroll bar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column = 2)
#Set scroll to listbox
HackerBox.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command= HackerBox.yview)

#Adding buttons
add_btn = Button(app, text="Add hacker",width = 12, command = add_item)
add_btn.grid(row= 2, column=0, pady =20)

#Run the window
app.mainloop()