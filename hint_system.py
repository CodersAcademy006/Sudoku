def provide_hint(board, solution, cells):
    """Fill in a logical hint for the next move."""
    for i in range(9):
        for j in range(9):
            if not cells[i][j].text() and solution[i][j]:
                cells[i][j].setText(str(solution[i][j]))
                return f"Hint: Cell ({i+1},{j+1}) filled."
    return "No hints available!"
