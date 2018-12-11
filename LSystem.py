from OpenGL.GLUT import *
from OpenGL.GLU  import *
from OpenGL.GL   import *
from math        import cos, sin, pi

SavedX       = list()
SavedY       = list()
SavedZ       = list()
SavedVectorX = list()
SavedVectorY = list()
SavedVectorZ = list()
SavedAngleLR = list()
SavedAngleUD = list()
currentX     = 0
currentY     = 0
currentZ     = 0
vectorX      = 0
vectorY      = 0
vectorZ      = 0
angleLR      = 90
angleUD      = 90
angle        = 35

def AddRules(rawRules):
    rules = {}
    # Iterates over each rule found in the received list
    for rule in rawRules:
        # We split the current rule in two
        splittedRule = rule.split("->")
        # And add both parts to a dictionary
        rules[splittedRule[0].strip()] = splittedRule[1].strip()

    return rules

def LSystem(axiom, rules, recursion):
    SetCoord()

    display = axiom

    # Apply the rules n times
    for i in range(recursion):
        aux = ""
        # Iterates over the current display string
        for c in display:
            # If the current char has an rule associated with it we apply it
            if c in rules.keys():
                aux += rules[c]
            # If it does not, we just add it to the new display string
            else:
                aux += c
        display = aux
    Draw(display)

def SetCoord():
    global currentX
    global currentY
    global currentZ
    
    global vectorX
    global vectorY
    global vectorZ

    global angleLR
    global angleUD
    
    currentX = 0
    currentY = 0
    currentZ = 0
    
    vectorX = 0
    vectorY = 1
    vectorZ = 0

    angleLR = 90
    angleUD = 90

def Draw(display):
    global SavedX
    global SavedY
    global SavedZ

    global SavedVectorX
    global SavedVectorY
    global SavedVectorZ

    global currentX
    global currentY
    global currentZ

    global vectorX
    global vectorY
    global vectorZ

    global angleLR
    global angleUD

    global angle

    glBegin(GL_LINES)

    # Iterates over the display string and draw what each char represents
    for letter in display:
        # Uses the vector to draw a line to the set angle
        if letter == 'F' or letter == 'G':
            glVertex3fv([currentX          , currentY          , currentZ])
            glVertex3fv([currentX + vectorX, currentY + vectorY, currentZ + vectorZ])
            currentX += vectorX
            currentY += vectorY
            currentZ += vectorZ
        # Sets the angle to the left
        elif letter == 'L':
            angleLR += angle
            vectorX  = cos(angleLR*pi/180)
            vectorY  = sin(angleLR*pi/180)
        # Sets the angle to the right
        elif letter == 'R':
            angleLR -= angle
            vectorX  = cos(angleLR*pi/180)
            vectorY  = sin(angleLR*pi/180)
        # Sets the angle closer to the screenc
        elif letter == 'U':
            angleUD += angle
            vectorZ  = cos(angleUD*pi/180)
            vectorY  = sin(angleUD*pi/180)
        # Sets the angle farther from the screen
        elif letter == 'D':
            angleUD -= angle
            vectorZ  = cos(angleUD*pi/180)
            vectorY  = sin(angleUD*pi/180)
        # Bookmarks the last position a line was drawn and its angle
        elif letter == '[':
            SavedX.append(currentX)
            SavedY.append(currentY)
            SavedZ.append(currentZ)
            SavedVectorX.append(vectorX)
            SavedVectorY.append(vectorY)
            SavedVectorZ.append(vectorZ)
            SavedAngleLR.append(angleLR)
            SavedAngleUD.append(angleUD)
        # Goes back to the last bookmarked position
        elif letter == ']':
            currentX = SavedX.pop()
            currentY = SavedY.pop()
            currentZ = SavedZ.pop()
            vectorX  = SavedVectorX.pop()
            vectorY  = SavedVectorY.pop()
            vectorZ  = SavedVectorZ.pop()
            angleLR  = SavedAngleLR.pop()
            angleUD  = SavedAngleUD.pop()
        else:
            continue

    glEnd()

def DisplayGL():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,0,3,0)
    LSystem(axiom, rules, recursion)
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
print("F: Desenha uma linha")
print("G: Desenha uma linha")
print("L: Move para a esquerda")
print("R: Move para a direita")
print("U: Move para cima")
print("D: Move para baixo")	
print("[: Guarda uma posicao")
print("]: Volta para a posicao guardada")
axiom     = raw_input("Entre com um axioma: ")
rawRules  = raw_input("Entre com as regras: ")
recursion = input("Entre com a quantidade de vezes que as regras serao aplicadas: ")
angle     = input("Entre com o angulo: ")

if ',' in rawRules:
    rules = AddRules(rawRules.split(','))
else:
    rules = AddRules([rawRules])

LSystem(axiom, rules, recursion)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("L-System")
glutDisplayFunc(DisplayGL)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(120,800.0/600.0,0.1,50.0)
glTranslatef(0.0,-7.5,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()