class LedCube(object):

	def __init__(self, shape, sensitivity):
		self.size = 8
		self.sensitivity = sensitivity
		self.internal_structure = [[[0 for z in range(self.size)] for y in range(self.size)]for x in range(self.size)]
		if shape == 'cube':
			self.create_cube()

	def create_cube(self):
		for z in range(self.size):
			if z in (2,3,4,5):
				for y in range(self.size):
					if y in (2,3,4,5):
						for x in range(self.size):
							if x in (2,3,4,5):
								self.internal_structure[x][y][z] = 1

	def get_direction(direction):
		for d in direction:
			d = d if abs(d) > self.sensitivity else 0
		return direction

	def move_internal(value, axis):


	def move(self, input_hash):
		direction = get_direction(input_hash['direction'])
		x, y, z = direction
		if x != 0:
			move_internal(x, "x")
		elif y != 0:
			move_internal(y, "y")
		elif z != 0:
			move_internal(z, "z")

		