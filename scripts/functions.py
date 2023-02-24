import numpy as np

RANDOM_SEED = None

def validate_RANDOM_SEED(
	RANDOM_SEED=RANDOM_SEED,
	):
	"""
	NEED TO DO:
	+ validate that this is an 'int' or 'None' type
	"""
	pass
	return None

def validate_LOW(
	low,
	):
	"""
	NEED TO DO:
	+ validate that this is a 'float' type
	"""
	pass
	return None

def validate_HIGH(
	high,
	):
	"""
	NEED TO DO:
	+ validate that this is a 'float' type
	"""
	pass
	return None

def generate_single_random_uniform(
	vector_length=1,
	low=0.0,
	high=1.0,
	random_seed=RANDOM_SEED,
	):

	assert vector_length == 1; "vector_length must be 1"
	
	validate_RANDOM_SEED(random_seed)
	if random_seed != None:
		np.random.seed(random_seed)
		random_uniform_vector = np.random.uniform(
			low=low,
			high=high,
			size=vector_length,
			)
	else:
		random_uniform_vector = np.random.uniform(
			low=low,
			high=high,
			size=vector_length,
			)
	
	
	return random_uniform_vector
	
