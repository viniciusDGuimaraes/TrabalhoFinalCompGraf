from OpenGL.GLUT import *
from OpenGL.GLU  import *
from OpenGL.GL   import *
from math        import cos, sin, pi

SavedX = 0
SavedY = 0
SavedZ = 0

SavedVectorX = 0
SavedVectorY = 0
SavedVectorZ = 0

currentX = 0
currentY = 0
currentZ = 0

vectorX = 0
vectorY = 0
vectorZ = 0

angleLR = 90
angleUD = 90

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

    # This variable will say what we should display in each iteration
    display = axiom
    # Apply the rules n times
    for i in range(recursion):
        print(display)
        Draw(display)
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

def SetCoord():
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

    SavedX = 0
    SavedY = 0
    SavedZ = 0
    
    SavedVectorX = 0
    SavedVectorY = 0
    SavedVectorZ = 0
    
    currentX = 0
    currentY = 0
    currentZ = 0
    
    vectorX = 0
    vectorY = 1
    vectorZ = 0

    angleLR = 0
    angleUD = 0

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

    glBegin(GL_LINES)

    # Iterates over the display string and draw what each char represents
    for letter in display:
        if letter == 'F':    
            glVertex3fv([currentX          , currentY          , currentZ])
            glVertex3fv([currentX + vectorX, currentY + vectorY, currentZ + vectorZ])
            currentX += vectorX
            currentY += vectorY
            currentZ += vectorZ
        elif letter == 'L':
            angleLR += 25
            vectorX  = cos(angleLR*pi/180)
            vectorY  = sin(angleLR*pi/180)
        elif letter == 'R':
            angleLR -= 25
            vectorX  = cos(angleLR*pi/180)
            vectorY  = sin(angleLR*pi/180)
        elif letter == 'U':
            angleUD += 25
            vectorZ  = cos(angleUD*pi/180)
            vectorY  = sin(angleUD*pi/180)
        elif letter == 'D':
            angleUD -= 25
            vectorZ  = cos(angleUD*pi/180)
            vectorY  = sin(angleUD*pi/180)
        elif letter == '[':
            SavedX       = currentX
            SavedY       = currentY
            SavedZ       = currentZ
            SavedVectorX = vectorX
            SavedVectorY = vectorY
            SavedVectorZ = vectorZ
        elif letter == ']':
            currentX = SavedX
            currentY = SavedY
            currentZ = SavedZ
            vectorX  = SavedVectorX
            vectorY  = SavedVectorY
            vectorZ  = SavedVectorZ
        else:
            continue

    glEnd()

def DisplayGL():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #glRotatef(2,1,3,0)
    LSystem(axiom, rules, recursion)
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
print("F: Desenha uma linha")
print("L: Move para a esquerda")
print("R: Move para a direita")
print("U: Move para cima")
print("D: Move para baixo")	
print("[: Guarda uma posicao")
print("]: Volta para a posicao guardada")
axiom     = raw_input("Entre com um axioma: ")
rawRules  = raw_input("Entre com as regras: ")
recursion = input("Entre com a quantidade de vezes que as regras serao aplicadas: ")

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
glTranslatef(0.0,0.0,-5)
glutTimerFunc(50,timer,1)
glutMainLoop()