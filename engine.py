from config import *

class Engine:
	'''
	Draws game scenes onto window.
	'''
	def __init__(self, width, height):
		'''
		Constructor to initialize raytracing context.

			Parameters:
				width (int): width of the screen
				height (int): height of the screen
		'''
		self.screenWidth = width
		self.screenHeight = height

		# General OpenGL configuration
		self.shader = self.createShader('shaders/frameBufferVertex.txt',
										'shaders/frameBufferFragment.txt')

		self.rayTracingShader = self.createComputeShader('shaders/rayTracer.txt')

		glUseProgram(self.shader)

		self.createQuad()
		self.createColorBuffer()

	def createQuad(self):
		'''
		Create quad.
		'''
		# x, y, z, s, t
		self.vertices = np.array((
				 1.0,  1.0, 0.0, 1.0, 1.0, # top-right
				-1.0,  1.0, 0.0, 0.0, 1.0, # top-left
				-1.0, -1.0, 0.0, 0.0, 0.0, # bottom-left
				-1.0, -1.0, 0.0, 0.0, 0.0, # bottom-left
				 1.0, -1.0, 0.0, 1.0, 0.0, # bottom-right
				 1.0,  1.0, 0.0, 1.0, 1.0), # top-right
				dtype=np.float32
			)