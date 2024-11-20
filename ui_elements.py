from PyQt5.QtWidgets import QGridLayout, QLineEdit
from PyQt5.QtCore import Qt
def create(grid_layout, cells):
    """Initialize and style the Sudoku grid UI."""
    for i in range(9):
        for j in range(9):
            cells[i][j] = QLineEdit()
            cells[i][j].setMaxLength(1)
            cells[i][j].setAlignment(Qt.AlignCenter)
            cells[i][j].setStyleSheet("font-size: 18px; border: 1px solid black;")
            grid_layout.addWidget(cells[i][j], i, j)