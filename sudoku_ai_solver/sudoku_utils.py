"""
Sudoku Utilities
Helper functions for display and formatting
"""

def print_grid(grid, title="Sudoku Grid"):
    """Print Sudoku grid in a readable format"""
    print("\n" + title)
    print("─" * 37)
    
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("├───────────┼───────────┼───────────┤")
        
        row_str = ""
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += "│ "
            
            if val == 0:
                row_str += ". "
            else:
                row_str += f"{val} "
        
        print(f"│ {row_str}│")
    
    print("─" * 37 + "\n")

def compare_grids(original, solved, expected=None):
    """Display original and solved grids side by side"""
    print("\n" + "="*80)
    print("PUZZLE COMPARISON")
    print("="*80)
    
    print("\nORIGINAL PUZZLE:" + " "*20 + "AI SOLUTION:")
    print("─" * 37 + "     " + "─" * 37)
    
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("├───────────┼───────────┼───────────┤" + "     " + 
                  "├───────────┼───────────┼───────────┤")
        
        # Original grid row
        orig_row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                orig_row += "│ "
            orig_row += f"{original[i][j] if original[i][j] != 0 else '.'} "
        
        # Solved grid row
        solved_row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                solved_row += "│ "
            solved_row += f"{solved[i][j] if solved[i][j] != 0 else '.'} "
        
        print(f"│ {orig_row}│     │ {solved_row}│")
    
    print("─" * 37 + "     " + "─" * 37)
    
    if expected:
        print("\nEXPECTED SOLUTION:")
        print("─" * 37)
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("├───────────┼───────────┼───────────┤")
            
            exp_row = ""
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    exp_row += "│ "
                exp_row += f"{expected[i][j]} "
            
            print(f"│ {exp_row}│")
        print("─" * 37)
    
    print("="*80 + "\n")

def get_difficulty_label(rating):
    """Convert numeric rating to difficulty label"""
    if rating <= 5:
        return "Easy"
    elif rating <= 20:
        return "Medium"
    elif rating <= 40:
        return "Hard"
    else:
        return "Expert"