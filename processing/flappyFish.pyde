from fish import Fish
from pipes import Pipe

fish = Fish()
pipes = []

def setup():
    size(640, 320)
    fish.loadPic()
    pipe = Pipe()
    pipes.append(pipe)

def draw():
    background(0, 153, 204)

    for i in range(len(pipes) - 1, -1, -1):
        if pipes[i].offscreen():
            pipes.pop(i)
        if pipes[i].collidesWith(fish):
            pipes[i].hilite = True
        else:
            pipes[i].hilite = False
        pipes[i].update()
        pipes[i].display()

    fish.update()
    fish.display()

    if (frameCount % 100 == 0):
        pipe = Pipe()
        pipes.append(pipe)

def keyPressed():
    if (key == " "):
        fish.up()