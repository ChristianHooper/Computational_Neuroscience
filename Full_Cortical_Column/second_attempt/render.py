import time
import glfw
import project_variables as sv
import controller as ct
from OpenGL.GL import *


def main():

    x_increase = 1.1 # Screen dimensions increase on x-axis
    y_increase = 3 # Screen dimensions increase on y-axis

    # Screen and render size
    screen_x = int(sv.DEPTH * x_increase) #  Cortical column z-depth, and x-axis window length
    screen_y = int(sv.WIDTH * y_increase) # Cortical column x & y width, and y-axis window length

    # Calculates offset based upon screen size, and the size of the cortical columns axis
    offset = lambda screen, axis: sv.normalize_zero(axis, screen, 0)

    offset_x = offset(screen_x, sv.DEPTH) # Offset for x-axis render
    offset_y = offset(screen_y, sv.WIDTH) # Offset for y-axs render


    # Initialize the library
    if not glfw.init():
        return

    # Window OpenGL
    window = glfw.create_window(screen_x, screen_y, "Six-Layered Cortical Column", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.set_window_pos(window, 256, 0) # Sets screen position
    glfw.make_context_current(window) # Make the window's context current

    glClearColor(0.0, 0.0, 0.0, 1.0) # Sets base color to black

    # Enable blending
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Depth testing is disabled if transparency doesn't work
    glDisable(GL_DEPTH_TEST)

    # Generates neurons, dendrite, axons in the morphological space
    ct.initialize_cortical_column()

    print("//////////[Real-Time Starts]//////////")

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT) # Clear screen

        glPointSize(2) # Sets the size of the point when drawn
        glColor3f(1.0, 1.0, 1.0) # Sets color of pixel

        glBegin(GL_POINTS) # Starts neuron render
        for neuron in ct.neural_array:

            # Applies layer color
            glColor3f(*neuron.color)


            # Draws neurons position in cortical column, (screen x = column z) & (screen y = column x)
            glVertex2f(sv.normalize(neuron.z, sv.DEPTH, 0) * offset_x, sv.normalize(neuron.x, sv.WIDTH, 0) * offset_y)

        glEnd() # Stops neuron render

        glfw.swap_buffers(window) # Swap front and back buffers

        # Events
        glfw.poll_events()
        time.sleep(.2)
    glfw.terminate()

if __name__ == "__main__":
    main()