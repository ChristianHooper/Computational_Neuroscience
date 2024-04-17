
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
# import voxel_data



# Vertex data: each vertex has 3 coordinates (x, y, z)
vertices = np.array([
    -0.5, -0.5, -0.5,  # Vertex 0
     0.5, -0.5, -0.5,  # Vertex 1
     0.5,  0.5, -0.5,  # Vertex 2
    -0.5,  0.5, -0.5,  # Vertex 3
    -0.5, -0.5,  0.5,  # Vertex 4
     0.5, -0.5,  0.5,  # Vertex 5
     0.5,  0.5,  0.5,  # Vertex 6
    -0.5,  0.5,  0.5   # Vertex 7
], dtype=np.float32)

# Indices for drawing cube faces using triangles (two triangles per face)
indices = np.array([
    0, 1, 2, 2, 3, 0,  # Front face
    1, 5, 6, 6, 2, 1,  # Right face
    5, 4, 7, 7, 6, 5,  # Back face
    4, 0, 3, 3, 7, 4,  # Left face
    3, 2, 6, 6, 7, 3,  # Top face
    4, 5, 1, 1, 0, 4   # Bottom face
], dtype=np.uint32)

# Vertex Shader
vertex_shader = """
#version 330 core
layout (location = 0) in vec3 aPos;
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;
void main()
{
    gl_Position = projection * view * model * vec4(aPos, 1.0);
}
"""

# Fragment Shader
fragment_shader = """
#version 330 core
out vec4 FragColor;
void main()
{
    FragColor = vec4(0.0, 0.0, 1.0, 1.0);  // White color
}
"""



# Initialize GLFW
if not glfw.init():
    raise Exception("GLFW cannot be initialized")

# Create window
window = glfw.create_window(800, 600, "Voxel Renderer", None, None)
if not window:
    glfw.terminate()
    raise Exception("GLFW window cannot be created")

glfw.make_context_current(window)

# Compile shaders
shader = compileProgram(compileShader(vertex_shader, GL_VERTEX_SHADER),
                        compileShader(fragment_shader, GL_FRAGMENT_SHADER))

# Initialize buffers and load data
vbo = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

ebo = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

# Generate VAO
vao = glGenVertexArrays(1)
glBindVertexArray(vao)
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)

# Unbind for safety
glBindBuffer(GL_ARRAY_BUFFER, 0)
glBindVertexArray(0)

glEnable(GL_DEPTH_TEST)  # Enable depth testing

# Rendering loop
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Use the shader program
    glUseProgram(shader)

    # Set the matrix uniforms
    identity_matrix = np.identity(4, dtype=np.float32)  # Create an identity matrix
    model_loc = glGetUniformLocation(shader, "model")
    view_loc = glGetUniformLocation(shader, "view")
    projection_loc = glGetUniformLocation(shader, "projection")

    glUniformMatrix4fv(model_loc, 1, GL_FALSE, identity_matrix)
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, identity_matrix)
    glUniformMatrix4fv(projection_loc, 1, GL_FALSE, identity_matrix)

    glBindVertexArray(vao)

    # Draw the cube
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    glfw.swap_buffers(window)
    glfw.poll_events()

# Terminate GLFW
glfw.terminate()




'''
# Initalize Pygame & OpenGL
pygame.init()
glutInit()
display = (1000, 1000)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Setup perspective
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Define dimensions
width, height, depth = 100, 100, 100

# Create a 3D numpy array initialized to 0 (empty)
voxel_grid = np.zeros((width, height, depth))

def draw_voxel(x, y, z):
    glPushMatrix()
    glTranslate(x - width/2, y - height/2, z - depth/2)
    glutSolidCube(1)  # Assume each voxel is a 1x1x1 cube
    glPopMatrix()

# Main render loop
while True:
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    for x in range(width):
        for y in range(height):
            for z in range(depth):
                voxel_grid[x][y][z] = random.randint(0, 1)
                if voxel_grid[x][y][z] == 1:
                    draw_voxel(x, y, z)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()
'''