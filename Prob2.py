########################################
# Name: Sage Soto
# Collaborators: N/A
# Estimated time spent (hrs): 1 hr and 5 min
########################################

from pgl import GWindow, GRect

WIDTH = 700
HEIGHT = 750
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

w = WIDTH               # Redefining constants for clarity
h = HEIGHT              #
bw = BRICK_WIDTH        #
bh = BRICK_HEIGHT       #
bib = BRICKS_IN_BASE    #

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    gw = GWindow(WIDTH, HEIGHT)
    
    # You got it from here
    
    total_rows = bib                # Total number of rows in the pyramid
    total_h = total_rows*bh         # Total height of the pyramid
    y0 = (h-total_h)//2             # Vertically centers the entire pyramid
    
    for row in range(total_rows):       # Loops over all the rows in the pyramid
        n_bricks = total_rows-row       # Calculates the number of bricks in a row
        x0 = (w-(n_bricks*bw))//2       # Horizontally centers the entire pyramid
        y = y0+(total_rows-row-1)*bh    # Determines the y-coordinate of any row
        for brick in range(n_bricks):   # Loops over all thr bricks in a row
            x = x0+(brick*bw)           # Determines the x-coordinate of any row
            rect = GRect(x,y,bw,bh)     # Defining a single brick
            gw.add(rect)                # Bricks are added to the graphics window 

if __name__ == '__main__':
    draw_pyramid()
