from datetime import datetime, timedelta
from .functions import *
import numpy as np
import pandas as pd
import time

class RandUniDF(object):
	"""docstring for ClassName"""
	def __init__(self, window_size=50, freq_in_secs=4, low=0.0, high=1.0, bias=0.0):
		super(RandUniDF, self).__init__()
		self.window_size = window_size
		self.freq_in_secs = freq_in_secs
		self.low = low
		self.high = high
		self.bias = bias
		self.run_wind_high = high
		self.run_wind_low = low
		self.df = pd.DataFrame(
			np.array( [np.NaN] * window_size), 
			columns=['y'],
			 )
		base = datetime.now()
		self.df['time_stamp'] = [base - timedelta(seconds=(1/4) * x) for x in range(window_size)[::-1]]

	def increment(self):
		self.df = self.df.shift(-1)
		self.df['time_stamp'].iloc[-1] = datetime.now()
		self.df['y'].iloc[-1] = generate_single_random_uniform(low=self.low, high=self.high) + self.bias
		self.run_wind_high = max(self.df['y'].max(), self.high)
		self.run_wind_low = min(self.df['y'].min(), self.low)

	def wait(self):
		time.sleep(1/self.freq_in_secs)

	def update_low(self, new_low):
		self.low = new_low 

	def update_high(self, new_high):
		self.high = new_high

	def update_bias(self, new_bias):
		self.bias = new_bias