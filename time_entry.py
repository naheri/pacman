import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title('TIME')

# Create a label to prompt the user for their name
label = tk.Label(window, text='How much time do you want the game to last (s) ? :')
label.pack()

# Create an entry field to input the name
entry = tk.Entry(window)
entry.pack()

# Create a function to be called when the user clicks the button
def get_time():
    global time_input
    # Get the value from the entry field
    time_input = entry.get()
    # Print the name to the console
    print(time_input)
    window.destroy()
    return time_input

# Create a button to submit the name
button = tk.Button(window, text='Submit', command=get_time)
button.pack()

# Run the Tkinter event loop
window.mainloop()