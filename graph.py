'''from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Open the text file
scores = []
with open('scores.txt', 'r') as f:
    # Read the contents of the file
    contents = f.read()
    print(contents)
    # Split the string into a list of lines
    lines = contents.split('\n')
    print(lines)
    # Initialize a variable to store the highest score
    highest_score = 0
    # Iterate over the list of lines
    for line in lines:
        # Split the line into a list of words
        words = line.split()
        scores.append(words[2])
# Create a Matplotlib figure
fig, ax = plt.subplots()

# Plot the scores as a line graph
ax.plot(scores)
def displayGraph():
    # Create a Tkinter window
    window = tk.Tk()
    window.title('graph')

    # Add the Matplotlib figure to the Tkinter window
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Run the Tkinter event loop
    window.mainloop()
'''