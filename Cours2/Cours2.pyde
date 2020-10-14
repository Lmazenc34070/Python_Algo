ballX = 0
ballY = 0
ballSpeedX = 3
ballSpeedY = 1
ballRadius = 5
racketX = 0
racketSize = 60
racketY = 0
racketHeight = 10

#ici on définit la fonction setup qui sera exécuté comme point d'entré dans mon code.
def setup():
    #on dit qu'on va faire appel à une variable
    global ballX, ballY, racketX, racketY, racketSize
    
    #ici on définit la taille de la fenêtre.
    size(400, 400)
    #on change le framerate
    frameRate(80)
    # on affecte une valeur de base a nos variables dans la fonctin setup
    ballX = width/2
    ballY = height/2
    
    
def draw():
    #on nettoie la fenêtre avant chaque nouveaux dessins
    clear()
    drawRacket()
    drawBall()
    
    
def drawRacket():
    global racketX, racketY, racketSize, racketHeight
    #On récupère les coordonnées de la souris
    #draw a rectangle in coords
    # x : mouseX minus half of width
    # y : height of the windows minus 20
    racketX = mouseX - racketSize / 2
    racketY = height - 20
    rect(racketX, racketY, racketSize, racketHeight)
    
def drawBall():
    global ballX, ballY, ballSpeedX, ballSpeedY, ballRadius, racketX, racketY, racketSize, racketHeight
    
    #La valeur des variables vont donc augmenter en permanence en étant appellées dans la fontcion Draw.
    #ballX = ballX + ballSpeedX
    #ballY = ballY + ballSpeedY
    #idem a ce qu'il y' au-dessus
    ballX += ballSpeedX
    ballY += ballSpeedY
    
    #Droite et gauche
    if(ballX + ballRadius > width ) :
        ballSpeedX *= -1
        ballX = width - ballRadius
    elif(ballX - ballRadius < 0) :
        ballSpeedX *= -1
        ballX = ballRadius
        
    #Bas et haut
    if(ballY + ballRadius > height) :
        ballSpeedY *= -1
        ballY = height- ballRadius
    elif(ballY - ballRadius < 0) :
        ballSpeedY *= -1
        ballY = ballRadius;
        
    if(racketY < ballY + ballRadius < racketY + racketHeight and ballSpeedY > 0) : #rebondis sur la position Y de la raquette et n'est pas replacé sur la raquette si la balle n'est pas en train de descendre
        if(racketX < ballX < racketX + racketSize):  #rebondis entre la position X de la raquette et la position X + la largeur de la raquette
               ballSpeedY *= -1
               ballY = racketY - ballRadius
                
    #draw circle centered on window
    circle(ballX, ballY, 2*ballRadius);
    
        
    
