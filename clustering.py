#!/usr/bin/env python3
""" clutsering.py
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import os


abspath = os.path.dirname(os.path.abspath(__file__))



def cluster(in_artifacts, out_artifacts):
	in_artifact1 = in_artifacts[0]
	in_artifact2 = in_artifacts[1]
	destination = out_artifacts[0].getLocation()
	pg_df = pd.read_csv(abspath + '/' + in_artifact1.getLocation())
	pg_2d_df = pd.read_csv(abspath + '/' + in_artifact2.getLocation())

	
	
	kmeans = KMeans(n_clusters=5)
	clusters = kmeans.fit(pg_df)

	pg_2d_df['cluster'] = pd.Series(clusters.labels_, index=pg_2d_df.index)
	pg_2d_df.to_csv(destination)
	return os.path.basename(__file__)
