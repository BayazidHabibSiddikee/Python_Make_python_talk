import tkinter as tk 

#Create window
root = tk.Tk()
root.title("This is window of tkinter")
root.geometry("800x200")

#Create label inside the window
label = tk.Label(text="This is a label",fg="Red",font=("Helvetica",80))
label.pack()

#run the game loop
root.mainloop()