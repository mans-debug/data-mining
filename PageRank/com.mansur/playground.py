import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(matrix.size)
# matrix[:, 2][1] = 20
# print(matrix[:, 2])
# def clean_dict(graph: dict):
#     for k, v in graph.items():
#         new_list = list()
#         [new_list.append(link) for link in v if link in graph]
#         graph[k] = new_list
#     return graph
#
#
# dic = {'AAAAAAAAAAAAAA': ['b', 'c', 'd', '5'],
#        'b': ['c', '3', 'AAAAAAAAAAAAAA'],
#        'c': ['AAAAAAAAAAAAAA', 'f', 'b']}
# dic = clean_dict(dic)
# [print(k + ": " + str(v)) for k, v in dic.items()]
#
# val_map = {
#     'AAAAAAAAAAAAAA': ['B', 'C', 'D'],
#     'B': ['AAAAAAAAAAAAAA', 'D'],
#     'C': ['AAAAAAAAAAAAAA'],
#     'D': ['B', 'C']
# }
# G = nx.DiGraph(directed=True)
# nodes = []
# for k, v in val_map.items():
#     [nodes.append((k, node)) for node in v]
# G.add_edges_from(nodes)
# pos = nx.spring_layout(G)
# # nx.draw_networkx_nodes(G, pos, node_size=50)
# # nx.draw_networkx_labels(G, pos)
# # nx.draw_networkx_edges(G, pos, edge_color='r', arrows=True)
# path = "C:\\Users\\mansu\\PycharmProjects\\PageRank\\resources\\graph-plot."
# nx.draw_networkx(G)
# plt.savefig(path + 'png', dpi=1000)
# plt.savefig(path + 'pdf', bbox_inches='tight')
# plt.show()

s = '123'
print(float('8.78842879e-05'))