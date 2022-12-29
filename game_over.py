from tkinter import *
from graph import displayGraph
HAUTEUR = 700
LARGEUR = 800
# Create a Tkinter window
window = Tk()
window.title('game over')
window.geometry('800x700')
# write a text at the top of the window
label = Label(window, text='GAME OVER/Le jeu est terminé !', font=('Helvetica', 30))
label.pack()
zoneBtn = Frame(window)
zoneBtn.grid(row=0,column=1,ipadx=5)
# button to display the graph
button = Button(window, text='Display the graph', command=displayGraph())
button.pack()
# button to restart the game
button = Button(window, text='Restart the game', command=window.destroy)
button.pack()
# button to quit the game
button = Button(window, text='Quit the game', command=window.destroy)
button.pack()
# Run the Tkinter event loop
window.mainloop()

