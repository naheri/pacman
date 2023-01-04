import tkinter as tk

def start_game():
    global player_name, game_time, num_players
    player_name = name_entry.get()
    game_time = time_entry.get()
    num_players = players_entry.get()
    window.destroy()
    
    # Do something with the player name, game time, and number of players
    print(f'Starting game with player {player_name}, game time {game_time} seconds, and {num_players} players')

# Create the main window
window = tk.Tk()
window.title('Game Launcher')

# Create the label and entry widgets for the player name
name_label = tk.Label(window, text='Enter your name:')
name_entry = tk.Entry(window)

# Create the label and entry widgets for the game time
time_label = tk.Label(window, text='Enter the game time in seconds:')
time_entry = tk.Entry(window)

# Create the label and entry widgets for the number of players
players_label = tk.Label(window, text='Enter the number of players (max 2):')
players_entry = tk.Entry(window)

# Create a button to start the game
start_button = tk.Button(window, text='Start Game', command=start_game)

# Add the widgets to the window
name_label.pack()
name_entry.pack()
time_label.pack()
time_entry.pack()
players_label.pack()
players_entry.pack()
start_button.pack()

# Run the Tkinter event loop
window.mainloop()
