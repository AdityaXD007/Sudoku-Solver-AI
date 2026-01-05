"""
Sudoku Utilities
Helper functions for display and formatting
"""

def print_grid(grid, title="Sudoku Grid"):
    """Print Sudoku grid in fancy box style"""
    print(f"\n{title}")
    print("┌─────────┬─────────┬─────────┐")
    
    for i, row in enumerate(grid):
        # Print horizontal separator every 3 rows
        if i > 0 and i % 3 == 0:
            print("├─────────┼─────────┼─────────┤")
        
        # Build row string
        row_str = "│"
        for j, val in enumerate(row):
            if val == 0:
                row_str += " . "
            else:
                row_str += f" {val} "
            
            # Add vertical separator every 3 columns
            if (j + 1) % 3 == 0:
                row_str += "│"
        
        print(row_str)
    
    print("└─────────┴─────────┴─────────┘\n")



def compare_grids(original, solved, expected=None):
    """Display original and solved grids side by side with clean formatting"""
    print("\n" + "="*80)
    print("PUZZLE COMPARISON")
    print("="*80)
    
    # Print headers
    print("\n" + "ORIGINAL PUZZLE".center(37) + "     " + "AI SOLUTION".center(37))
    print("┌─────────┬─────────┬─────────┐     ┌─────────┬─────────┬─────────┐")
    
    for i in range(9):
        if i > 0 and i % 3 == 0:
            print("├─────────┼─────────┼─────────┤     ├─────────┼─────────┼─────────┤")
        
        # Original grid row
        orig_row = "│"
        for j in range(9):
            val = original[i][j]
            orig_row += f" {val if val != 0 else '.'} "
            if (j + 1) % 3 == 0 and j < 8:
                orig_row += "│"
        orig_row += "│"
        
        # Solved grid row
        solved_row = "│"
        for j in range(9):
            val = solved[i][j]
            solved_row += f" {val if val != 0 else '.'} "
            if (j + 1) % 3 == 0 and j < 8:
                solved_row += "│"
        solved_row += "│"
        
        print(f"{orig_row}     {solved_row}")
    
    print("└─────────┴─────────┴─────────┘     └─────────┴─────────┴─────────┘")
    
    if expected:
        print("\nEXPECTED SOLUTION:")
        print("┌─────────┬─────────┬─────────┐")
        for i in range(9):
            if i > 0 and i % 3 == 0:
                print("├─────────┼─────────┼─────────┤")
            
            exp_row = "│"
            for j in range(9):
                val = expected[i][j]
                exp_row += f" {val} "
                if (j + 1) % 3 == 0 and j < 8:
                    exp_row += "│"
            exp_row += "│"
            
            print(exp_row)
        print("└─────────┴─────────┴─────────┘")
    
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