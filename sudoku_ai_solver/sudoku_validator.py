"""
Sudoku Validator - Constraint Checking
Implements row, column, and sub-grid constraints
"""

GRID_SIZE = 9
SUBGRID_SIZE = 3

class SudokuValidator:
    
    @staticmethod
    def is_valid(grid, row, col, num):
        """
        Check if placing 'num' at (row, col) is valid
        Returns: True if valid, False otherwise
        """
        # Check row constraint
        if num in grid[row]:
            return False
        
        # Check column constraint
        for i in range(GRID_SIZE):
            if grid[i][col] == num:
                return False
        
        # Check 3x3 sub-grid constraint
        start_row = (row // SUBGRID_SIZE) * SUBGRID_SIZE
        start_col = (col // SUBGRID_SIZE) * SUBGRID_SIZE
        
        for i in range(start_row, start_row + SUBGRID_SIZE):
            for j in range(start_col, start_col + SUBGRID_SIZE):
                if grid[i][j] == num:
                    return False
        
        return True
    
    @staticmethod
    def verify_solution(grid):
        """
        Verify if the complete grid is a valid Sudoku solution
        Returns: (is_valid, error_messages)
        """
        errors = []
        
        # Check all rows
        for row in range(GRID_SIZE):
            if sorted(grid[row]) != list(range(1, 10)):
                errors.append(f"Row {row + 1} is invalid")
        
        # Check all columns
        for col in range(GRID_SIZE):
            column = [grid[row][col] for row in range(GRID_SIZE)]
            if sorted(column) != list(range(1, 10)):
                errors.append(f"Column {col + 1} is invalid")
        
        # Check all 3x3 sub-grids
        for box_row in range(0, GRID_SIZE, SUBGRID_SIZE):
            for box_col in range(0, GRID_SIZE, SUBGRID_SIZE):
                subgrid = []
                for i in range(box_row, box_row + SUBGRID_SIZE):
                    for j in range(box_col, box_col + SUBGRID_SIZE):
                        subgrid.append(grid[i][j])
                
                if sorted(subgrid) != list(range(1, 10)):
                    errors.append(f"Sub-grid at ({box_row // 3 + 1}, {box_col // 3 + 1}) is invalid")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def is_complete(grid):
        """Check if grid has no empty cells"""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if grid[row][col] == 0:
                    return False
        return True