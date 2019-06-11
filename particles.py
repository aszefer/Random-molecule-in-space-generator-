import numpy
from math import sqrt

# Generate a random seed
numpy.random.seed()

class Particle():
	""" A class represting a signle particle """
	min_offset = 1.0

	def __init__(self, index, symbol = "C", pos = (0,0,0)):
		self.pos = ((numpy.random.rand(3) - 0.5) * 30)
		self.symbol = symbol
		self.is_main = None # Flag for checking if it's primary
		self.main_particle = None # Index of primary particle
		self.offset = [0,0,0] # Offset to the secondary particle
		self.index = index # Own index

	def next_frame(self):
		""" Move to next frame """
		width = 30 # total width
		limit = 15 # total width divided by 2
		dim = 3 # number of dimensions
		a = self.get_pos()

		# Subtract 0.5 to make the generated value to be from -0.5 to 0.5
		# Multiply by 4 to make the steps a bit bigger, up to 2.0
		b = ((numpy.random.rand(dim) - 0.5) * 4)
		c = a + b

		for index in range(0,dim):
			if (c[index] > limit):
				c[index] = c[index] - width + self.offset[index]

			if (c[index] < (limit * -1)):
				c[index] = c[index] + width - self.offset[index]

		self.pos = c
		#return b

	def move(self):
		# Check if the particle is the 'main' particle in a dimer
		# or if it's not in a dimer
		if self.is_main or self.is_main == None:
			self.next_frame()

	def child_move(self, particle):
		""" Move child (not main in a dimer) to fathers position + offset """
		if self.is_main == False:
			a = particle.get_pos()
			b = self.offset
			c = numpy.array(a) + numpy.array(b) # new child's pos = parent's position + offset
			self.set_pos(c)
			self.try_destroy_dimer(particle)

	def find_dimer(self, particles):
		if self.is_main == None:
			# iterate through all particles but start from the current particle
			for particle in particles[self.index:]:
				# Only if it's main, not in a dimer and not itself
				if self.is_main == None 
			and particle.get_is_main() == None 
			and self.get_index() != particle.get_index():
					a = particle.get_pos()
					b = self.get_pos()
					# Calculate the distance between two vectors
					c = (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2
					c = sqrt(c)
					offset = numpy.array(b) - numpy.array(a)

					if c <= self.min_offset:
						# Create a dimer
						# Give the child particle index of father
						particle.main_particle = self.get_index()
						# Set current particle as a father/main
						self.set_is_main(True)
						# Set the found particle as a child in the dimer
						particle.set_is_main(False)
						# Finally set offset
						particle.set_offset(offset)
						break

	def try_destroy_dimer(self, particle):
		if  self.is_main == False:
			random = numpy.random.rand(1)[0]
			if random > 0.5:
				self.main_particle = None
				self.set_is_main(None)
				particle.set_is_main(None)
				self.set_offset([0,0,0])

	def get_pos(self):
		return self.pos

	def set_pos(self, pos):
		self.pos = pos

	def set_offset(self, offset):
		self.offset = offset

	def get_index(self):
		return self.index

	def get_is_main(self):
		return self.is_main

	def set_is_main(self, is_main):
		self.is_main = is_main

	def get_main_particle(self):
		return self.main_particle

	def get_data(self):
		""" Return data line formatted for .XYZ file """
		pos = self.get_pos()
		pos = ' '.join(str(p) for p in pos)
		data = self.symbol
		data += ' '
		data += pos
		return data


if __name__ == "__main__":
	print("This isn't an executable!")
