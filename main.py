import sys
from PyQt6.QtWidgets import QApplication

import GUI
import palettes

app = QApplication(sys.argv)
app.setStyle("Fusion")
app.setPalette(palettes.dark_palette())

window = GUI.Window()
window.show()
sys.exit(app.exec())
