from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def LSystem():
    pass

def DisplayGL():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    LSystem()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
print("0: Desenha uma linha que termina em uma folha")
print("1: Desenha uma linha")	
print("[: Move 25 graus para a esquerda")
print("]: Move 25 graus para a direita")
axiom    = str(input("Entre com um axioma: "))
rawRules = str(input("Entre com as regras: "))
if ',' in rawRules:
    rules = addRules([rawRules])
else:
    rules = addRules(rawRules.split(','))
rules    = rawRules.split(',')

input()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("L-System")
glutDisplayFunc(DisplayGL)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(90,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-5)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
