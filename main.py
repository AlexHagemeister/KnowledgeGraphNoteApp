# main.py

# Import QApplication from PyQt6.QtWidgets for the application framework
from PyQt6.QtWidgets import QApplication
# Import the GraphWindow class from your graph_window.py file
from graph_window import GraphWindow
# Import the sys module for system-specific parameters and functions
import sys

# Check if this script is the entry point to the program
if __name__ == "__main__":
    # Create a new QApplication object; this is required for any PyQt6 application
    app = QApplication(sys.argv)

    # Create an instance of your custom GraphWindow class
    window = GraphWindow()

    # Show the window on the screen
    window.show()

    # Start the application's event loop and exit when it's done
    sys.exit(app.exec())
