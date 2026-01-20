"""
Sudoku Dataset Manager
Handles loading, filtering, and preprocessing of Sudoku puzzles
Supports both train.csv and test.csv datasets
"""

import pandas as pd
import numpy as np

class SudokuDataset:
    def __init__(self, csv_path='train.csv'):
        """
        Initialize dataset manager
        csv_path: Path to your dataset ('train.csv' or 'test.csv')
        """
        self.csv_path = csv_path
        self.df = None
        self.filtered_df = None
    
    def load_dataset(self, nrows=None):
        """
        Load the complete dataset
        nrows: Load only first N rows (useful for huge datasets)
        """
        print(f"Loading dataset from {self.csv_path}...")
        
        if nrows:
            # Load only specified number of rows for speed
            self.df = pd.read_csv(self.csv_path, nrows=nrows)
            print(f"Loaded first {nrows} puzzles (subset)")
        else:
            # Load entire dataset (may take time for 30M rows)
            self.df = pd.read_csv(self.csv_path)
        
        print(f"Total puzzles loaded: {len(self.df)}")
        print(f"Columns: {list(self.df.columns)}")
        return self.df
    
    def filter_dataset(self, n_samples=5000, difficulty_range=None, random_state=42):
        """
        Filter dataset to desired size
        
        Parameters:
        - n_samples: Number of puzzles to select (default 5000)
        - difficulty_range: Tuple (min_rating, max_rating) or None for all
        - random_state: Random seed for reproducibility
        """
        if self.df is None:
            # Load only what we need for efficiency
            # Load 10x more than needed to ensure good random sample
            self.load_dataset(nrows=n_samples * 10)
        
        # Apply difficulty filter if specified
        if difficulty_range:
            min_rating, max_rating = difficulty_range
            filtered = self.df[(self.df['rating'] >= min_rating) & 
                             (self.df['rating'] <= max_rating)]
        else:
            filtered = self.df
        
        # Random sampling
        if len(filtered) > n_samples:
            self.filtered_df = filtered.sample(n=n_samples, random_state=random_state)
        else:
            self.filtered_df = filtered
        
        print(f"Filtered to {len(self.filtered_df)} puzzles")
        
        # Show difficulty distribution
        print(f"\nDifficulty distribution:")
        print(f"  Min rating: {self.filtered_df['rating'].min()}")
        print(f"  Max rating: {self.filtered_df['rating'].max()}")
        print(f"  Average rating: {self.filtered_df['rating'].mean():.2f}")
        
        return self.filtered_df
    
    def save_filtered_dataset(self, output_path='sudoku_filtered.csv'):
        """Save filtered dataset to new CSV"""
        if self.filtered_df is not None:
            self.filtered_df.to_csv(output_path, index=False)
            print(f"Filtered dataset saved to {output_path}")
    
    def parse_puzzle(self, puzzle_string):
        """
        Convert puzzle string to 9x9 grid
        '.' or '0' represents empty cells
        """
        # Replace dots with zeros
        puzzle_string = puzzle_string.replace('.', '0')
        
        # Convert to list of integers
        digits = [int(d) for d in puzzle_string]
        
        # Reshape to 9x9 grid
        grid = np.array(digits).reshape(9, 9).tolist()
        
        return grid
    
    def get_random_puzzle(self):
        """Get a random puzzle from filtered dataset"""
        if self.filtered_df is None:
            self.filter_dataset()
        
        row = self.filtered_df.sample(n=1).iloc[0]
        
        puzzle_grid = self.parse_puzzle(row['question'])
        solution_grid = self.parse_puzzle(row['answer'])
        
        return {
            'puzzle': puzzle_grid,
            'solution': solution_grid,
            'rating': row['rating'],
            'source': row['source']
        }
    
    def get_puzzle_by_index(self, index):
        """Get specific puzzle by index"""
        if self.filtered_df is None:
            self.filter_dataset()
        
        row = self.filtered_df.iloc[index]
        
        puzzle_grid = self.parse_puzzle(row['question'])
        solution_grid = self.parse_puzzle(row['answer'])
        
        return {
            'puzzle': puzzle_grid,
            'solution': solution_grid,
            'rating': row['rating'],
            'source': row['source']
        }