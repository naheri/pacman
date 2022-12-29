import tkinter as tk
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Open the text file
with open('scores.txt', 'r') as f:
    # Read the contents of the file
    contents = f.read()

# Split the string into a list of lines
lines = contents.split('\n')

# Initialize a dictionary to store the scores for each player
scores = {}

# Iterate over the list of lines
for line in lines:
    # Split the line into a list of words
    words = line.split()
    # Split the line into a list of words
    score = int(words[2])
    player_name = words[0]
    # Add the score to the dictionary
    if player_name in scores:
        scores[player_name].append(score)
    else:
        scores[player_name] = [score]
print("scores: ",scores)
# Sort the players by the highest score
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print("the sorted scores :", sorted_scores)
# Get the names of the 2 best players
best_players = [player_name for player_name, _ in sorted_scores[:2]]
print("the best_players are ", best_players)
game_number = min(len(scores[best_players[0]]), len(scores[best_players[1]]))
x = [i for i in range(game_number)]
default_x_ticks = range(len(x))
plt.plot(default_x_ticks)
# Create a Matplotlib figure
fig, ax = plt.subplots()

# Plot the scores for each player as a line graph
for player_name in best_players:
    ax.plot(scores[player_name], label=player_name)
# Add a legend to the graph
ax.legend()

# Set the x-axis label
ax.set_xlabel('Game Number')

# Set the y-axis label
ax.set_ylabel('Score')

# Create a Tkinter window named "graph"
def displayGraph():
    window = tk.Tk()
    window.title('graph')

    # Add the Matplotlib figure to the Tkinter window
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Run the Tkinter event loop
    window.mainloop()

