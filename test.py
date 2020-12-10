from BRTree import BRTree
import networkx as nx
import matplotlib.pyplot as plt

red_nodes = []
black_nodes = []
def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.value] = (x, y)
    print(node.value, node.color, " ", pos)
    if node.color == 0:
        red_nodes.append(node.value)
    else:
        black_nodes.append(node.value)
    if node.left:
        G.add_edge(node.value, node.left.value)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.value, node.right.value)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)

def draw(node):  # 以某个节点为根画图
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节

    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    nx.draw_networkx_edges(graph, pos, alpha=0.5, width=1)
    nx.draw_networkx_nodes(graph, pos, nodelist=red_nodes, node_color="tab:red",label=node.value)
    nx.draw_networkx_nodes(graph, pos, nodelist=black_nodes, node_color="tab:gray",label=node.value)

    plt.show()

print("red nodes", red_nodes)
print("black nodes", black_nodes)
red_nodes = []
black_nodes = []
brt = BRTree()
brt.insert(11)
red_nodes = []
black_nodes = []
draw(brt.root)
brt.insert(14)
red_nodes = []
black_nodes = []
draw(brt.root)
brt.insert(7)
red_nodes = []
black_nodes = []
draw(brt.root)
brt.insert(9)
red_nodes = []
black_nodes = []
draw(brt.root)
brt.insert(8)
red_nodes = []
black_nodes = []
draw(brt.root)
brt.insert(3)
red_nodes = []
black_nodes = []
draw(brt.root)
brt.insert(15)
red_nodes = []
black_nodes = []
draw(brt.root)


brt.delete(11)
red_nodes = []
black_nodes = []
draw(brt.root)

brt.delete(8)
red_nodes = []
black_nodes = []
draw(brt.root)
