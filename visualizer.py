#!/usr/bin/env python3
""" visualizer.py
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

abspath = os.path.dirname(os.path.abspath(__file__))

def visualize(in_artifacts, out_artifacts):
	# Define the names of each column in the tweets file
	
	in_artifact = in_artifacts[0]
	in_artifact2 = in_artifacts[1]
	out_artifact1 = out_artifacts[0]
	out_artifact2 = out_artifacts[1]
	# out_artifact3 = out_artifacts[2]

	pg_2d_df = pd.read_csv(abspath + '/' + in_artifact.getLocation())
	pg_df = pd.read_csv(abspath + '/' + in_artifact2.getLocation())


	
	ax = pg_2d_df.plot(kind='scatter', x='PC2', y='PC1', figsize=(16,8))
	for i, country in enumerate(pg_df.index):
	    ax.annotate(
	        country, 
	        (pg_2d_df.iloc[i].PC2, pg_2d_df.iloc[i].PC1)
	    )
	plt1 = sns.regplot(ax=ax, data=pg_2d_df, x='PC2', y='PC1')
	fig1 = plt1.get_figure()
	plt2 = sns.lmplot(x="PC2", y="PC1", hue="cluster", data=pg_2d_df, size = 10, fit_reg=False)
	fig2 = plt2.fig
	# plt3 = sns.clustermap(data=pg_2d_df)
	# fig3 = plt3.fig

	fig1.savefig(out_artifact1.getLocation())
	fig2.savefig(out_artifact2.getLocation())
	# fig3.savefig(out_artifacts3.getLocation())
	return os.path.basename(__file__)




