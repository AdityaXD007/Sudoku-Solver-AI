"""
Sudoku Metrics Tracker
Tracks and reports performance metrics
"""

import time
import pandas as pd

class MetricsTracker:
    def __init__(self):
        self.results = []
    
    def track_solve(self, puzzle_data, solver_metrics, execution_time, 
                   solution_correct, solved_grid):
        """Record metrics for a single solve attempt"""
        result = {
            'puzzle_rating': puzzle_data['rating'],
            'puzzle_source': puzzle_data['source'],
            'execution_time': execution_time,
            'max_recursion_depth': solver_metrics['max_recursion_depth'],
            'backtrack_count': solver_metrics['backtrack_count'],
            'solution_correct': solution_correct,
            'solved': solved_grid is not None
        }
        
        self.results.append(result)
        return result
    
    def get_summary_statistics(self):
        """Calculate summary statistics across all tracked solves"""
        if not self.results:
            return None
        
        df = pd.DataFrame(self.results)
        
        summary = {
            'total_puzzles': len(df),
            'solved_count': df['solved'].sum(),
            'solve_rate': (df['solved'].sum() / len(df)) * 100,
            'avg_time': df['execution_time'].mean(),
            'max_time': df['execution_time'].max(),
            'min_time': df['execution_time'].min(),
            'avg_recursion_depth': df['max_recursion_depth'].mean(),
            'avg_backtracks': df['backtrack_count'].mean(),
            'correct_solutions': df['solution_correct'].sum()
        }
        
        return summary
    
    def export_results(self, filename='solver_results.csv'):
        """Export results to CSV"""
        if self.results:
            df = pd.DataFrame(self.results)
            df.to_csv(filename, index=False)
            print(f"Results exported to {filename}")
    
    def print_solve_report(self, result):
        """Print detailed report for a single solve"""
        print("\n" + "="*60)
        print("SOLVE REPORT")
        print("="*60)
        print(f"Puzzle Source: {result['puzzle_source']}")
        print(f"Difficulty Rating: {result['puzzle_rating']}")
        print(f"\nPerformance Metrics:")
        print(f"  • Execution Time: {result['execution_time']:.4f} seconds")
        print(f"  • Max Recursion Depth: {result['max_recursion_depth']}")
        print(f"  • Backtrack Count: {result['backtrack_count']}")
        print(f"\nResult:")
        print(f"  • Solved: {'✓ Yes' if result['solved'] else '✗ No'}")
        print(f"  • Solution Correct: {'✓ Yes' if result['solution_correct'] else '✗ No'}")
        print("="*60 + "\n")
    
    def print_summary(self):
        """Print summary statistics"""
        summary = self.get_summary_statistics()
        
        if summary is None:
            print("No results to summarize")
            return
        
        print("\n" + "="*60)
        print("SUMMARY STATISTICS")
        print("="*60)
        print(f"Total Puzzles Attempted: {summary['total_puzzles']}")
        print(f"Puzzles Solved: {summary['solved_count']}")
        print(f"Solve Rate: {summary['solve_rate']:.2f}%")
        print(f"\nTiming Statistics:")
        print(f"  • Average Time: {summary['avg_time']:.4f} seconds")
        print(f"  • Fastest Solve: {summary['min_time']:.4f} seconds")
        print(f"  • Slowest Solve: {summary['max_time']:.4f} seconds")
        print(f"\nAlgorithm Statistics:")
        print(f"  • Avg Recursion Depth: {summary['avg_recursion_depth']:.2f}")
        print(f"  • Avg Backtracks: {summary['avg_backtracks']:.2f}")
        print(f"  • Correct Solutions: {summary['correct_solutions']}")
        print("="*60 + "\n")