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
    if contents == '':
        print('No scores yet!')
    else:
        print(f'\n\nContents of scores.txt: {contents}')
        # Split the string into a list of lines
        lines = contents.split('\n')
        # Remove the last element of the list, which is an empty string
        lines.pop()
        print(f'List of lines: {lines}')
        # Initialize a dictionary to store the scores for each player
        scores = {}

        # Iterate over the list of lines
        for line in lines:
            # Split the line into a list of words
            words = line.split()
            print(f'Line: {line}')
            print(f'List of words: {words}')
            # Split the line into a list of words
            score = int(words[2])
            player_name = words[0]
            # Add the score to the dictionary
            if player_name in scores:
                scores[player_name].append(score)
            else:
                scores[player_name] = [score]
        # Sort the players by the highest score
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        # Get the names of the 2 best players
        best_players = [player_name for player_name, _ in sorted_scores[:2]]
        # Get the number of games played
        game_number = max(len(scores[best_players[0]]),len(scores[best_players[1]]))
        x = list(range(1, game_number + 1))
        # get the number of games played for each player
        game_number = enumerate(scores[best_players[0]], start=1)
        # Create a list of x-axis tick labels

        plt.plot()
        # Create a Matplotlib figure
        fig, ax = plt.subplots()

        # Plot the scores for each player as a line graph
        for player_name in best_players:
            ax.plot(scores[player_name], label=player_name)
        # Add a legend to the graph
        ax.legend()

        # Set the x-axis label
        ax.set_xlabel('Game Number')
        ax.set_xticks(x)
        ax.set_xticklabels(x)
        # Set the y-axis label
        ax.set_ylabel('Score')

# Create a Tkinter window named "graph"
def displayGraph():
    window = tk.Tk()
    window.title('graph')
    print(f'x: {x}')
    print(f'best_players: {best_players}')
    print(f'number of games (max): {max(len(scores[best_players[0]]),len(scores[best_players[1]]))}')
    print(f'game_number: {list(enumerate(scores[best_players[0]], start=1))}')

    # Add the Matplotlib figure to the Tkinter window
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Run the Tkinter event loop
    window.mainloop()

