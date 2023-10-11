# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas, scene_width, scene_height, 1)
    draw_cloud(canvas, 350, 150, 350, 100)
    draw_cloud(canvas, 370, 165, 370, 110)
    draw_cloud(canvas, 400, 100, 50, 50)
    draw_cloud(canvas, 400, 175, 100, 75)
    draw_cloud(canvas, 325, 250, 150, 50)
    draw_cloud(canvas, 360, 450, 150, 50)
    draw_cloud(canvas, 400, 550, 75, 50)
    draw_cloud(canvas, 380, 600, 150, 50)
    draw_cloud(canvas, 360, 575, 150, 50)
    draw_cloud(canvas, 340, 565, 50, 50)
    draw_cloud(canvas, 325, 100, 200, 50)
    draw_cloud(canvas, 300, 400, 50, 50)
    draw_sun(canvas, 400, 100, 150, 150)
    draw_ground(canvas, scene_width, 150, 1)
    draw_tree(canvas, 650, 0, 450)
    draw_tree(canvas, 550, 0, 450)
    for x in range(25, 800, 44):
        fence(canvas, x, 0, 180)

    for i in range(0, 800, 10):
        draw_grass(canvas, i, 0, 100)

    for j in range(5, 790, 25):
        draw_grass(canvas, j, 0, 200)

    for k in range(2, 792, 12):
        draw_light_grass(canvas, k, 0, 150)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_tree(canvas, center, bottom, height):
    # drawing the tree trunk
    twidth = height / 10
    theight = height / 5
    tleft = center - twidth / 2
    tbottom = bottom
    tright = center + twidth / 2
    ttop = bottom + theight
    draw_rectangle(canvas, tleft, tbottom, tright, ttop, fill="saddlebrown", outline="saddlebrown")

    swidth = height / 2
    sleft = center - swidth / 2
    sbottom = ttop
    sright = center + swidth / 2
    scenter = center
    stop = bottom + height
    draw_polygon(canvas, sleft, sbottom, scenter, stop, sright, sbottom, fill="green", outline="green")

def draw_grass(canvas, center, bottom, height):
    gwidth = height / 15
    gheight = height / 5
    gleft = center - gwidth / 2
    gbottom = bottom
    gright = center + gwidth / 2
    gtop = bottom + gheight
    draw_rectangle(canvas, gleft, gbottom, gright, gtop, fill="green3", outline="green3")

def draw_light_grass(canvas, center, bottom, height):
    gwidth = height / 20
    gheight = height / 5
    gleft = center - gwidth / 2
    gbottom = bottom
    gright = center + gwidth / 2
    gtop = bottom + gheight
    draw_rectangle(canvas, gleft, gbottom, gright, gtop, fill="green1", outline="green1")

def draw_sky(canvas, width, height, interval):
    # draw sky
    for x in range(0, width, interval):
        draw_line(canvas, x, 0, x, height, fill="sky blue")

def draw_ground(canvas, width, height, interval):
    # draw sky
    for x in range(0, width, interval):
        draw_line(canvas, x, 0, x, height, fill="brown")


def draw_cloud(canvas, x, y, diameter, diameter1):
    x_axis = y
    y_axis = x
    draw_oval(canvas, x_axis, y_axis, x_axis + diameter, y_axis + diameter1 , outline="white", fill="white")

def draw_sun(canvas, x, y, diameter, diameter1):
    x_axis = y
    y_axis = x
    draw_oval(canvas, x_axis, y_axis, x_axis + diameter, y_axis + diameter1 , outline="yellow", fill="yellow")

def fence(canvas, center, bottom, height):
    fwidth = height / 5
    fheight = height / 1
    fleft = center - fwidth / 2
    fbottom = bottom
    fright = center + fwidth / 2
    ftop = bottom + fheight
    draw_rectangle(canvas, fleft, fbottom, fright, ftop, fill="white", outline="white")

    twidth = height / 2
    sleft = center - twidth / 2
    sbottom = ftop
    sright = center + twidth / 2
    scenter = center
    stop = bottom + height
    draw_polygon(canvas, sleft, sbottom, scenter, stop, sright, sbottom, fill="white", outline="white")

# Call the main function so that
# this program will start executing.
main()