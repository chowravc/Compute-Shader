from config import *
import engine

class App:
    '''
    Calls high level control functions (handle input, draw scene, etc.)
    '''
    def __init__(self):
        '''
        Constructor for application object.
        '''
        pg.init()

        self.screenWidth = 800
        self.screenHeight = 600
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode((self.screenWidth, self.screenHeight), pg.OPENGL|pg.DOUBLEBUF)
        self.graphicsEngine = engine.Engine(self.screenWidth, self.screenHeight)

        self.lastTime = pg.time.get_ticks()
        self.currentTime = 0
        self.numFrames = 0
        self.frameTime = 0
        self.lightCount = 0

        self.mainLoop()

    def mainLoop(self):
        '''
        Game loop within application.
        '''
        running = True
        while(running):

            # Events
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    running = False
                if(event.type == pg.KEYDOWN):
                    if(event.key == pg.K_ESCAPE):
                        running = False

            # Render
            self.graphicsEngine.renderScene()

            # Timing
            self.calculateFramerate()

    def calculateFramerate(self):
        '''
        Calculate running framerate of game.
        '''
        self.currentTime = pg.time.get_ticks()
        delta = self.currentTime - self.lastTime
        if(delta >= 1000):
            framerate = max(1, int(1e3 * self.numFrames / delta))
            pg.display.set_caption(f"Running at {framerate} Hz.")
            self.lastTime = self.currentTime
            self.numFrames = -1
            self.frameTime = float(1e3 / max(1, framerate))
        self.numFrames += 1

    def quit(self):
        '''
        Exiting the application.
        '''
        pg.quit()

if __name__ == '__main__':
    myApp = App()
    myApp.run()
    myApp.quit()