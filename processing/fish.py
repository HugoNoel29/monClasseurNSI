class Fish:


    def __init__(self):

        self.x = 50 #abscisse

        self.y = 240 #ordonnée

        self.r = 32 #taille


        self.gravity = 0.6 #pesanteur

        self.lift = -12 #acenseur 

        self.velocity = 0 #accélération 


    def loadPic(self):

        self.pic = loadImage("poisson.png")

    def up(self):

        self.velocity += self.lift


    def display(self):

        image(self.pic, self.x, self.y)

    def update(self):

        self.velocity += self.gravity

        self.velocity *= 0.9

        self.y += self.velocity

        if (self.y >= height - self.r):

            self.y = height - self.r

            self.velocity = 0

        elif (self.y <= 0):

            self.y = 0

            self.velocity = 0