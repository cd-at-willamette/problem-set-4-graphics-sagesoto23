########################################
# Name: Sage Soto
# Collaborators: N/A
# Estimate time spent (hrs): 1 hour and 40 min
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():
    
    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function
    
    gw = GWindow(GW_WIDTH, GW_HEIGHT)                   # Creates the graphics window
    box = GRect(SQUARE_SIZE,SQUARE_SIZE)                # Creating the initial center box
    box.set_filled(True)                                # Completely fills the box with a color
    box.set_color("Blue")                               # This box will always be blue
    x0 = GW_WIDTH/2                                     # Center x-coordinate of the window
    y0 = GW_HEIGHT/2                                    # Center y-coordinate of the window
    gw.add(box,x0-(SQUARE_SIZE/2),y0-(SQUARE_SIZE/2))   # Adds the blue box to the center of the window
    
    count = 0                                   # Local count of the score before clicking 
    score = GLabel(f'{count}')                  # Creating the score label
    score.set_font(SCORE_FONT)                  # Sets the score to a certain font
    gw.add(score,SCORE_DX,55-SCORE_DY)          # Adds the label to the window
    
    def move_box():                                     # This function will randomly move the box around
        xn = random.randint(0,GW_WIDTH-SQUARE_SIZE)     # A random x-coordinate is chosen within the window
        yn = random.randint(0,GW_HEIGHT-SQUARE_SIZE)    # A random y-coordinate is chosen within the window
        box.set_location(xn,yn)                         # The blue box's location will change to the random coordinates
        
    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        count = 0                                   # Another local count of the score after clicking
        x,y = event.get_x(),event.get_y()           # When clicked, an x and y coordinate is returned 
        if box.contains(x,y):                       # If these coordinates are located within the blue box
            count += 1                              # The score increases by 1
            score.set_label(f'{count}')             # The label changes in accordance with the score
            move_box()                              # The blue box moves to a random location
        else:                                       # If these coordinates are not in the blue box
            count = 0                               # The score returns to 0
            score.set_label(f'{count}')             # The label changes in accordance with the score
    gw.add_event_listener("click",on_mouse_down)    # The code will perform when the user clicks on the window

if __name__ == '__main__':
    clicky_box()
