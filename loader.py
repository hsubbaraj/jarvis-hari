#!/usr/bin/env python3
""" loader.py
"""
import pandas as pd
import numpy as np
import os

def load(in_artifacts, out_artifacts, data_source):
	destination = out_artifacts[0].getLocation()
	# Define the names of each column in the tweets file
	
	pg_df = pd.read_csv(data_source, index_col = 0)
	pg_df = pg_df.drop(['Pos','Tm'], axis=1)
	pg_df = pg_df.dropna(how='any')
	pg_df.to_csv(destination, index=False, header=False)

def load_data(in_artifacts, out_artifacts):
	load(in_artifacts, out_artifacts, 'pg_stats.csv')
	return os.path.basename(__file__)

