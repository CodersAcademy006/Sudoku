def apply_theme(theme_name, cells):
    """Apply the selected theme to the Sudoku board."""
    if theme_name == "Dark":
        style = "background-color: black; color: white;"
    elif theme_name == "Neon":
        style = "background-color: black; color: lime;"
    else:
        style = "background-color: white; color: black;"
    
    for row in cells:
        for cell in row:
            cell.setStyleSheet(style)
