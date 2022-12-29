# Open the text file
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
        highest_score = max(highest_score, int(words[2]))
    print("the highest score is ", highest_score)

