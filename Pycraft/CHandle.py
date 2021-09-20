from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def MapModel(Map, Map_scale, Map_trans, map_vertices):
    glPushMatrix() 
    glScalef(*Map_scale) 
    glTranslatef(*Map_trans)
    for mesh in Map.mesh_list: 
        glBegin(GL_TRIANGLES)
        for i in range(0, len(arrayStorage)):
            glVertex3f(*arrayStorage[i], sep = ',')
        glEnd()
    glPopMatrix()