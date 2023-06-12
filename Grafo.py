import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)

G.add_edge(0,1,weight=2)
G.add_edge(1,2,weight=8)
G.add_edge(3,0,weight=5)
G.add_edge(3,1,weight=9)
G.add_edge(3,4,weight=5)
G.add_edge(3,5,weight=1)
G.add_edge(4,2,weight=5)
G.add_edge(4,1,weight=1)
G.add_edge(5,4,weight=3)
G.add_edge(5,6,weight=1)
G.add_edge(6,4,weight=1)

pos = nx.spring_layout(G, seed = 1, scale = 7) 

nx.draw_networkx_nodes(G, pos)

nx.draw_networkx_edges(G, pos)

nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)   

try: 
    print(nx.dijkstra_path(G,5,2))
    print(nx.dijkstra_path_length(G,5,2))
        
except nx.NetworkXNoPath:
   print("Erro! Nao existe o caminho selecionado")

plt.show()


