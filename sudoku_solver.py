"""
Sudoku AI Solver - Core Algorithm
Uses Minimum Remaining Values (MRV) heuristic with Backtracking
"""

import copy

# Constants
GRID_SIZE = 9
SUBGRID_SIZE = 3
EMPTY_CELL = 0

class SudokuSolver:
    def __init__(self):
        self.recursion_depth = 0
        self.backtrack_count = 0
        self.max_recursion_depth = 0
    
    def solve(self, grid):
        """
        Main solving function using MRV + Backtracking
        Returns: (solved_grid, success_flag)
        """
        self.recursion_depth = 0
        self.backtrack_count = 0
        self.max_recursion_depth = 0
        
        grid_copy = copy.deepcopy(grid)
        success = self._solve_recursive(grid_copy)
        
        return grid_copy, success
    
    def _solve_recursive(self, grid):
        """Recursive backtracking solver with MRV heuristic"""
        self.recursion_depth += 1
        self.max_recursion_depth = max(self.max_recursion_depth, self.recursion_depth)
        
        # Find cell with minimum remaining values (MRV)
        cell = self._find_mrv_cell(grid)
        
        # Base case: No empty cell found (puzzle solved)
        if cell is None:
            self.recursion_depth -= 1
            return True
        
        row, col = cell
        
        # Get valid domain for this cell
        domain = self._get_domain(grid, row, col)
        
        # Dead end: no valid values
        if not domain:
            self.recursion_depth -= 1
            return False
        
        # Try each value in domain
        for num in domain:
            grid[row][col] = num
            
            # Recursive call
            if self._solve_recursive(grid):
                self.recursion_depth -= 1
                return True
            
            # Backtrack
            grid[row][col] = EMPTY_CELL
            self.backtrack_count += 1
        
        self.recursion_depth -= 1
        return False
    
    def _find_mrv_cell(self, grid):
        """Find empty cell with minimum remaining values (MRV heuristic)"""
        min_domain_size = float('inf')
        best_cell = None
        
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if grid[row][col] == EMPTY_CELL:
                    domain = self._get_domain(grid, row, col)
                    domain_size = len(domain)
                    
                    if domain_size < min_domain_size:
                        min_domain_size = domain_size
                        best_cell = (row, col)
                    
                    # Optimization: if domain size is 1, return immediately
                    if domain_size == 1:
                        return best_cell
        
        return best_cell
    
    def _get_domain(self, grid, row, col):
        """Calculate valid domain (possible values) for a cell"""
        from sudoku_validator import SudokuValidator
        
        validator = SudokuValidator()
        domain = []
        
        for num in range(1, 10):
            if validator.is_valid(grid, row, col, num):
                domain.append(num)
        
        return domain
    
    def get_metrics(self):
        """Return performance metrics"""
        return {
            'max_recursion_depth': self.max_recursion_depth,
            'backtrack_count': self.backtrack_count
        }