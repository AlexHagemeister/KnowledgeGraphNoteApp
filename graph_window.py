# graph_window.py

# Import the necessary PyQt6 modules for the GUI
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit
# Import QWebEngineView to embed a web view in the application
from PyQt6.QtWebEngineWidgets import QWebEngineView

# Import QUrl to handle URLs
from PyQt6.QtCore import QUrl
# Import the GraphManager class to manage the graph
from graph_manager import GraphManager

# Define the GraphWindow class, inheriting from QWidget (a base class for all UI objects in PyQt)
class GraphWindow(QWidget):
    def __init__(self):
        # Initialize the QWidget base class
        super(GraphWindow, self).__init__()

        # Create a QVBoxLayout to manage the layout of widgets vertically
        layout = QVBoxLayout()

        # Create a QWebEngineView widget to display HTML content
        self.web_view = QWebEngineView()


        # Load the local HTML file into the web view
        # self.web_view.load(QUrl.fromLocalFile("custom.html"))
        self.web_view.load(QUrl.fromLocalFile("graphtest.html")) # FIXME: test

        # Add the web view to the layout
        layout.addWidget(self.web_view)

        # Create a QLineEdit widget for the text box
        self.text_box = QLineEdit()
        # Connect the 'returnPressed' event to the 'on_text_entered' method
        self.text_box.returnPressed.connect(self.on_text_entered)

        # Add the text box to the layout
        layout.addWidget(self.text_box)

        # Create an instance of the GraphManager class to manage the graph
        self.graph_manager = GraphManager()

        # Set the layout for this QWidget
        self.setLayout(layout)

    # Define what happens when text is entered in the text box and Enter is pressed
    def on_text_entered(self):
        # Get the text from the text box
        command = self.text_box.text()

        # Check if the command starts with "add "
        if command.startswith("add "):
            
            # Extract the node name from the command
            node_name = command[4:]

            print(f"Adding a node with name '{node_name}'")

            # Add the node using the GraphManager instance
            self.graph_manager.add_node(node_name, node_name)

            print(f"Added a node with name '{node_name}'")

            # Reload the web view to reflect the changes in the graph
            self.web_view.reload()
