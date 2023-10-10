# graph_manager.py

from pyvis.network import Network

class GraphManager:
    def __init__(self):
        self.net = Network()

    def add_node(self, node_id, label):
        self.net.add_node(node_id, label=label)
        # self.to_html("/Users/alexhagemeister/PROGRAMMING/Python/KnowledgeGraphStuff/graph_app_1.0/custom.html")
        self.to_html("/Users/alexhagemeister/PROGRAMMING/Python/KnowledgeGraphStuff/graph_app_1.0/graphtest.html")  # FIXME: test

    def add_edge(self, from_id, to_id):
        self.net.add_edge(from_id, to_id)
        # self.to_html("/Users/alexhagemeister/PROGRAMMING/Python/KnowledgeGraphStuff/graph_app_1.0/custom.html")  
        self.to_html("/Users/alexhagemeister/PROGRAMMING/Python/KnowledgeGraphStuff/graph_app_1.0/graphtest.html") # FIXME: test

    def to_html(self, path):
        print(self.net)
        try:
            self.net.show(path)
            with open(path, 'r') as f:
                html = f.read()
            # Replace CDN URLs here
            with open(path, 'w') as f:
                f.write(html)
        except Exception as e:
            print("An error occurred:", e)

        self.net.show(path, notebook=False)
