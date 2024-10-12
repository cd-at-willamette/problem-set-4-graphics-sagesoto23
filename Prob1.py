############################################################
# Name: Sage Soto
# Name(s) of anyone worked with: N/A
# Est time spent (hr): 1 hr and 25 min
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 800
HEIGHT = 400

w = WIDTH
h = HEIGHT

def draw_image():
    """ Creates a window and draws a student's creation"""
    # Creating the window
    gw = GWindow(w, h)
    
    def rectangle(x,y,w,h,color):           # Defining any rectangle in the window
        r = GRect(x,y,w,h)                  # Rectangle has x,y coordinates and dimensions
        r.set_filled(True)                  # Completely colors the rectangle
        r.set_color(color)                  # Chooses a specific color if called
        gw.add(r)                           # Adds the rectangle to the window

    def rect_rotate(x,y,w,h,color,theta):   # Defining any rectangle that will be angled
        p = GRect(x,y,w,h)                  # Also has x,y coordinates and dimensions
        p.set_filled(True)                  # Gets fully colored one color
        p.set_color(color)                  # Choose any specific color
        p.rotate(theta)                     # Choose any specific angle to rotate the rectangle
        gw.add(p)                           # Adds the rectangle to the window
   
    # Following Lines Create the Background Layer of the Union Jack
    rectangle(0,0,w-450,h//2.005,"White")           
    rectangle(0,0,w-450,h//2.005,"Blue")            
    rect_rotate(20,-18,w-400,h//8.5,"White",-30)    
    rect_rotate(0,175,w-400,h//8.5,"White",30)      
    rectangle(0,0,15,16,"White")                    
    rectangle(0,175,25,25,"White")                  
    
    # Following Lines Create the 8 Stripes
    rectangle(350,0,450,h//8,"White")       
    rectangle(350,50,450,h//7,"Red")        
    rectangle(350,100,450,h//6,"Blue")      
    rectangle(350,150,450,h//5,"White")     
    rectangle(0,200,w,h//4,"Red")           
    rectangle(0,250,w,h//3,"Blue")          
    rectangle(0,300,w,h//2,"White")         
    rectangle(0,350,w,h,"Red")              
    
    # Following Lines Complete the Union Jack
    rect_rotate(0,200,w-600,h//25,"Red",30)     
    rect_rotate(0,-3,w-600,h//25,"Red",-30)
    rect_rotate(147,100,w-550,h//25,"Red",30)
    rect_rotate(175,83,w-550,h//25,"Red",-30)
    rectangle(350,150,450,h//8.15,"White")
    
    rectangle(0,65,w-450,h//5.45,"White")           # Two white cross stripes
    rectangle(137.5,0,w//10.75,h//2.005,"White")
    rectangle(0,77.5,w-450,h//8.5,"Red")            # Two red cross strips
    rectangle(150,0,w//16,h//2,"Red")
      
    #circle(0,0,w//4,h//5,"Purple")
    #line(0,w//2,w,h//2)
    #label("How long can this string go?",w//2,h//2)
      
if __name__ == '__main__':
    draw_image()
