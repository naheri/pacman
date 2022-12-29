import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title('name')

# Create a label to prompt the user for their name
label = tk.Label(window, text='Enter your name:')
label.pack()

# Create an entry field to input the name
entry = tk.Entry(window)
entry.pack()

# Create a function to be called when the user clicks the button
def on_button_click():
    global name_input
    # Get the value from the entry field
    name_input = entry.get()
    # Print the name to the console
    print(name_input)
    window.destroy()
    return name_input

# Create a button to submit the name
button = tk.Button(window, text='Submit', command=on_button_click)
button.pack()

# Run the Tkinter event loop
window.mainloop()
