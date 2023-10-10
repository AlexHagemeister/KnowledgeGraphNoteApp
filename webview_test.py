from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys

class SimpleWindow(QWidget):
    def __init__(self):
        super(SimpleWindow, self).__init__()

        # Create a QVBoxLayout to manage the layout
        layout = QVBoxLayout()

        # Create a QWebEngineView widget to display HTML content
        web_view = QWebEngineView()

        # Load the local HTML file into the web view
        web_view.load(QUrl.fromLocalFile("/Users/alexhagemeister/PROGRAMMING/Python/KnowledgeGraphStuff/graph_app_1.0/graphtest.html"))
        # web_view.load(QUrl.fromLocalFile("/Users/alexhagemeister/PROGRAMMING/Python/KnowledgeGraphStuff/graph_app_1.0/simplehtml.html"))

        # Add the web view to the layout
        layout.addWidget(web_view)

        # Set the layout for this QWidget
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec())
