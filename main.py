import streamlit as st
import numpy as np
import pandas as pd
import scripts.functions
from scripts.objects import RandUniDF
from plotly.express import scatter

def app():
	
	with st.sidebar:
		window_size = st.number_input(
			label="Select window size", 
			min_value=10, 
			max_value=100,
			value=50,
			step=1,
			key='window_size',
			)

		freq_in_secs = st.slider(
			label="Select generation frequency, in seconds", 
			min_value=1, 
			max_value=8,
			value=4,
			step=1,
			key='freq_in_secs',
			)

	@st.cache(allow_output_mutation=True)
	def inital_df(
		window_size=window_size, 
		freq_in_secs=freq_in_secs,
		):
		df = RandUniDF(
			window_size=window_size, 
			freq_in_secs=freq_in_secs,
			)
		return df

	range_low = st.slider(
		label="Select lowest possible value", 
		min_value=-10., 
		max_value=10.,
		value=0.,
		step=0.01,
		format="%.2f",
		key='range_low',
		)

	range_high = st.slider(
		label="Select highest possible value", 
		min_value=-10., 
		max_value=10.,
		value=1.,
		step=0.01,
		format="%.2f",
		key='range_low',
		)

	range_bias = st.slider(
		label="Select bias to add to all values value", 
		min_value=-10., 
		max_value=10.,
		value=0.,
		step=0.01,
		format="%.2f",
		key='range_bias',
		)

	show_df_progress = st.checkbox(
		label="show DataFrame progress",
		value=False,
		key='show_df_progress',
		)

	start_stream = st.checkbox(
		"start_stream",
		value=False,
		key='start_stream',
		)

	if start_stream:
		randUniDF = inital_df()
		df_plot = st.empty()
		df_output = st.empty()
		while True:
			randUniDF.update_low(new_low=range_low)
			randUniDF.update_high(new_high=range_high)
			randUniDF.update_bias(new_bias=range_bias)
			randUniDF.increment()
			randUniDF.wait()
			# if show_initial_df:
			with df_plot:
				# fig = randUniDF.df.plot.scatter(y='y', x='time_stamp', plotnonfinite=True).figure
				# st.pyplot(fig)
				if randUniDF.run_wind_low < 0:
					ymin = randUniDF.run_wind_low * 1.2
				else:
					ymin = randUniDF.run_wind_low * 0.8

				if randUniDF.run_wind_high < 0:
					ymax = randUniDF.run_wind_high * 0.8
				else:
					ymax = randUniDF.run_wind_high * 1.2

				fig = scatter(
					data_frame=randUniDF.df,
					y='y', 
					x='time_stamp',
					range_y=[ymin , ymax],
					)
				st.plotly_chart(fig)
			if show_df_progress:
				with df_output:
					st.write(randUniDF.df)


	# 	df = df.shift(-1)





if __name__ == "__main__":
    app()