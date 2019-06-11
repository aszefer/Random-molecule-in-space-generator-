import particles


def one_step(pc):
	for p in pc:
		if p.get_is_main() or p.get_is_main() == None:
			p.move()
			p.find_dimer(pc)
		else:
			father_index = p.get_main_particle()
			p.child_move(pc[father_index])

def step_to_file(fname, pc):
	with open(fname, 'a') as file:
		file.write(str(len(pc)) + '\n')
		file.write('\n')
		for p in pc:
			file.write(p.get_data() + '\n')



# Simulation settings
file_name = "output.xyz"
step_count = 600

# Clear file if exists
open(file_name, 'w').close()

# Prepare variables for simulation
particle_count = 10
pc1 = [] # 'pc' for 'particle container'

# Fill container with particles
for index in range(0,particle_count):
	pc1.append(particles.Particle(index))

# Save the first step
step_to_file(file_name, pc1)

# loop for all steps
for index in range(1,step_count):
	one_step(pc1)
	step_to_file(file_name, pc1)
