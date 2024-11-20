from reportlab.pdfgen import canvas

def save_puzzle_to_file(filename, board):
    """Save the puzzle to a file."""
    with open(filename, "w") as f:
        for row in board:
            f.write(" ".join(str(num) if num != 0 else "." for num in row) + "\n")

def print_sudoku_to_pdf(filename, board):
    """Export the Sudoku puzzle to a PDF."""
    pdf = canvas.Canvas(filename)
    pdf.drawString(100, 800, "Sudoku Puzzle")
    y = 700
    for row in board:
        pdf.drawString(100, y, " ".join(str(num) if num != 0 else "." for num in row))
        y -= 20
    pdf.save()
