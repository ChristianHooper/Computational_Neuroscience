import time
import glfw
import system_variables as sv
import controller as ct
from OpenGL.GL import *

'''
[ROAD MAP]
2. (Need to add spacial replacement in morphospace array for axon segments )
3. Dendrite generation & behavoiur
4. Cell type behavoius specificity
5. Soma neural functionaility
6. Neurite cell functionaily (growth/puning)

Data input, how, what?  

Time steps?? Hertz influence, but local in calucations
'''

def main():

    # Screen and render size
    depth = 1600 #  Cortical column z-depth, and x-axis window length
    width = 50 # Cortical column x & y width, and y-axis window length

    depth_offset = depth/2
    width_offset = width/2

    # Returns a normalized value of a input from a given range
    def norm(value, max=1, min=0):
        return (2 * ((value - min)/(max - min)) - 1)


    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(depth, width, "Six-Layered Cortical Column", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.set_window_pos(window, 100, 0)

    # Make the window's context current
    glfw.make_context_current(window)

    # Sets base color to black
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Enable blending and set the blending function before entering the drawing loop
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Ensure depth testing is disabled if transparency doesn't work properly with depth testing
    glDisable(GL_DEPTH_TEST)

    ct.initialize() # Generates neurons, dedrite, axons in the morphological space


    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT) # Clear screen
        
        glPointSize(3) # Sets the size of the point when drawn
        glColor3f(1.0, 1.0, 1.0) # Sets color of pixel

        glBegin(GL_POINTS) # Starts render
        for neuron in ct.position_dictionary.values():
            
            # Applies Neuron color
            glColor3f(*neuron.color)
            #print(neuron.type)
            # Draws neurons position in cortical column with fliped x & y (x=depth)
            glVertex2f(norm(neuron.id[2], depth, 0), norm(neuron.id[0], width, 0))
             # Grows one new neural segment
            #print(neuron.axon.length_array)

            #print(norm(neuron.id[0], width), norm(neuron.id[2], depth))
            #glVertex2f(neuron.id[1], neuron.id[2])
        glEnd()

        
        
        for neuron in ct.position_dictionary.values():
            axon = neuron.axon
            axon.axonogenesis()
            
            
            glColor4f(1.0, 0.5, 0.5, 0.4)
            glBegin(GL_LINES)
            for section in range(axon.axon_head): # Get the current number of segments in axon
                
                location = axon.length_array[section] # Gets axons segment location
                #location[0:+3]
                glVertex2f(norm(location[2], depth, 0), norm(location[0], width, 0)) # (x, y)
            glEnd()
            # NEEDS to draw each segment of the axon in the length array START HERE
            #glVertex2f(norm(axon.length_array[axon.axon_head][2], depth, 0)/10,
            #norm(axon.length_array[axon.axon_head][0], width, 0)/10)
        
        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()
        time.sleep(.2)
    glfw.terminate()

if __name__ == "__main__":
    main()