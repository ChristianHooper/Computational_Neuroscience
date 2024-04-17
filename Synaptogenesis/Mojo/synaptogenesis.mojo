from python import Python

fn main() raises:
    var plt = Python.import_module("matplotlib")
    var np = Python.import_module("numpy")
    var pg = Python.import_module("pygame")
    var gl = Python.import_module("OpenGL.GL")
    
    print("Working.")

    np.array_space = np.zeros((100, 100, 100)) # Creates a 100^3 area space.


    # Access the element at position (1, 2, 3)
    # element = array_space[1, 2, 3]

    # Modify the element at position (1, 2, 3)
    # array_space[1, 2, 3] = 10

    var vertices: PythonObject = ( # Tuples w/ tuples
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

    var edges: PythonObject = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (4,5),
    (5,6),
    (6,7),
    (7,4),
    (0,4),
    (1,5),
    (2,6),
    (3,7)
    )

    # Intialize Pygame
    pg.pygame.init()
    var display: PythonObject = (800, 800) # Declares as python obejct to be called in OpenGL function call.

    
    pg.pygame.display.set_mode(display, gl.DOUBLEBUF|gl.OPENGL) # Sets up the display for OpenGL.
    gl.gluPersepective(45, (display[0]/display[1]), 0.1, 50.0) # Defines veiwport distortion.
    gl.Translatef(0.0, 0.0, -5)

    def draw_cube():
        gl.glBegin(gl.GL_LINES) # OpenGLinterpret each pair of vertices as begin/endpoints of a straight line.
        for edge in edges:
            for vertex in edge:
                gl.glVertex3fv(vertices[vertex]) # Specifies Begining & End verticies for vertex.
        gl.glEnd()

    while True:
        for event in pg.pygame.event.get():
            if event.type == pg.pygame.QUIT:
                pg.pygame.quit()
                pg.quit()
        
        gl.glRotatef(1, 3, 1, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pg.ptgame.display.flip()
        pg.pygame.time.wait(10)











