from pyvis.network import Network

# Create a new network
net = Network()

# Add nodes
# The 'value' attribute will be used to set the size of the node
net.add_node(1, label="Node 1", value=0)
net.add_node(2, label="Node B", value=0)
net.add_node(3, label="Node C", value=0)
net.add_node(4, label="Node D", value=0)

# Add edges
net.add_edge(1, 2)
net.add_edge(2, 3)
net.add_edge(3, 4)
net.add_edge(4, 1)
net.add_edge(1, 3)

# Update node sizes based on their degree
for node_id in net.nodes:
    node_id['value'] = len(net.get_adj_list()[node_id['id']])

# Show the network
net.show("simple_network.html", notebook=False)


