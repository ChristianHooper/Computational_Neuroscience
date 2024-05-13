import glfw
from OpenGL.GL import *

def main():

    # Initialize GLFW (Returns early if there's an issue)
    if not glfw.init():
        return

    # Creates window
    window = glfw.create_window(1000, 1000, "Draw a Transparent Pixel", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current (Render window in current thread)
    glfw.make_context_current(window)

    # Set the viewport
    glViewport(0, 0, 1000, 1000)

    # Set the clear color to black
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Enable blending for transparency
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    while not glfw.window_should_close(window):
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Set the color with transparency (RGBA)
        glColor4f(1.0, 1.0, 1.0, 0.5)  # 50% transparency

        # Draw one pixel
        glPointSize(1)  # Make it bigger to see the effect clearly
        glBegin(GL_POINTS)
        glVertex2f(0.0, 0.0)  # Coordinates of the pixel
        glEnd()

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()