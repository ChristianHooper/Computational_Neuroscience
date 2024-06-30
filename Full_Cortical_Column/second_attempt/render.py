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

    glfw.set_window_pos(window, 256, 512) # Sets screen position
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

    while not glfw.window_should_close(window): # Render-loop
        sv.set_time() #Start render timer

        # If true neural structure will render
        if sv.render == True: # Runs rendering of entire cortical column
            glClear(GL_COLOR_BUFFER_BIT) # Clear screen

            for neuron in ct.neural_array: # Selects each neuron for rendering

                glPointSize(3) # Sets the size of the point when drawn
                glBegin(GL_POINTS) # Starts neuron render
                glColor3f(*neuron.color) # Applies layer color for neuron based upon layer
                # Draws neurons position in cortical column, (screen x = column z) & (screen y = column x)
                glVertex2f(sv.normalize(neuron.z, sv.DEPTH, 0) * offset_x, sv.normalize(neuron.x, sv.WIDTH, 0) * offset_y)
                glEnd() # Ends neuron render

                glPointSize(1) # Sets size for axon and dendrite render
                glBegin(GL_POINTS) # Renders the axons of the selected neuron
                for i in range(neuron.axon.head+1): # Evaluates each segment in axon
                    segment = neuron.axon.genesis_array[i]
                    # Neural y-axis scaling shader (DISABLE BY DEFAULT; EXPENSIVE)
                    #neuron.axon.color = [channel * (segment[1] * 0.01) + 0.3 for channel in neuron.axon.color]
                    glColor4f(*neuron.axon.color, 0.5) # Defines axon color in lieu of shader
                    # Renders neuron on screen with offset after cortical position normalization
                    glVertex2f(sv.normalize(segment[2], sv.DEPTH, 0) * offset_x, sv.normalize(segment[0], sv.WIDTH, 0) * offset_y)
                glEnd() # Stops neuron render

                # Renders the dendrites of the selected neuron
                glBegin(GL_POINTS)
                for i in range(neuron.dendrite.head+1):
                    segment = neuron.dendrite.genesis_array[i]
                    # Neural y-axis scaling shader (EXPENSIVE)
                    #neuron.axon.color = [channel * (segment[1] * 0.01) + 0.3 for channel in neuron.axon.color]
                    glColor4f(*neuron.dendrite.color, 0.5)
                    glVertex2f(sv.normalize(segment[2], sv.DEPTH, 0) * offset_x, sv.normalize(segment[0], sv.WIDTH, 0) * offset_y)
                glEnd() # Stops neuron render

        ct.cortical_functions() # Grows existing axonal segment by one

        glfw.swap_buffers(window) # Swap front and back buffers

        # Events
        glfw.poll_events()
        sv.get_time() # Times render per cycle
        #time.sleep(.1) # Column minimum time steps

    glfw.terminate()

if __name__ == "__main__":
    main()