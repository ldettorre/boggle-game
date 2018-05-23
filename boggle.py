from string import ascii_uppercase
from random import choice

def make_grid(cols, rows):
    return {(c, r): choice(ascii_uppercase) 
                    for c in range(cols) 
                    for r in range(rows)}

def get_neighbours(pos):
    col, row = pos
    return [
            (col-1, row-1), 
            (col, row-1),
            (col+1, row-1),
            (col+1, row),
            (col+1, row+1),
            (col, row+1),
            (col-1,row+1),
            (col-1,row),
            ]
            
def all_grid_neighbours(grid):
    return {pos: [ n for n in get_neighbours(pos) if n in grid] for pos in grid}

def path_to_word(grid, path):
    word = ""
    for pos in path:
        word+= grid[pos]
    return word
    
def read_wordfile(filename):
    f = open(filename,"r")
    text = f.read().upper()
    words = text.split("\n")
    # words = f.read().split("\n")
    # words = [w.upper() for w in words]
    f.close()
    return words

print(read_wordfile("bogwords.txt"))