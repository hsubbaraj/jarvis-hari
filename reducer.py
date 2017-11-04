#!/usr/bin/env python3
""" reducer.py
"""
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

import os, pickle

abspath = os.path.dirname(os.path.abspath(__file__))



def dim_reduce(in_artifacts, out_artifacts):
	

	in_artifact = in_artifacts[0]
	out_artifact1 = out_artifacts[0]
	out_artifact2 = out_artifacts[1]
	out_artifact3 = out_artifacts[2]
	pg_df = pd.read_csv(abspath + '/' + in_artifact.getLocation())
	# Define the names of each column in the tweets file
	
	pca = PCA(copy=True, n_components=2, whiten=False)
	pca.fit(pg_df)
	pg_2d = pca.transform(pg_df)
	pg_2d_df = pd.DataFrame(pg_2d)
	pg_2d_df.index = pg_df.index
	pg_2d_df.columns = ['PC1','PC2']

	
	components = pca.components_
	ex_var = pca.explained_variance_
	ex_var_ratio = pca.explained_variance_ratio_
	# sing_val = pca.singular_values_
	with open(abspath + "/" + out_artifact1.getLocation(), "wb") as f:
		
		pickle.dump(components, f)
		pickle.dump(ex_var, f)
		pickle.dump(ex_var_ratio, f)
		# pickle.dump(sing_val, f)

	with open(abspath + "/" + out_artifact3.getLocation(), "wb") as g:
		np.savetxt(g, components, fmt='%.18e')
		np.savetxt(g, ex_var)
		np.savetxt(g, ex_var_ratio)


	pg_2d_df.to_csv(out_artifact2.getLocation())


	return os.path.basename(__file__)
