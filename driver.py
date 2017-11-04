#!/usr/bin/env python3
import jarvis1

from loader import load_data
from reducer import dim_reduce
from clustering import cluster
from visualizer import visualize

data_loader = jarvis1.Action(load_data)
pg_data = jarvis1.Artifact('pg_statistics.csv', data_loader)


data_dim_reducer = jarvis1.Action(dim_reduce, [pg_data])
reduced_components_pkl = jarvis1.Artifact('reduced_data.pkl', data_dim_reducer) 
reduced_pg_data = jarvis1.Artifact('reduced_pg_data.csv', data_dim_reducer)
reduced_components_txt = jarvis1.Artifact('reduced_data.txt', data_dim_reducer) 

cluster_action = jarvis1.Action(cluster, [pg_data, reduced_pg_data])
clustered_data = jarvis1.Artifact('clustered_pg_data.csv', cluster_action)

data_visualizer = jarvis1.Action(visualize, [clustered_data, pg_data])
visuals1 = jarvis1.Artifact('plt1.png', data_visualizer)
visuals2 = jarvis1.Artifact('plt2.png', data_visualizer)
# visuals3 = jarvis1.Artifact('plt3.png', data_visualizer)

visuals1.pull()
visuals2.pull()



