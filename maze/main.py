import sys
import os

from maze import Maze

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python maze.py [maze.txt]")
        sys.exit(1)

    if not os.path.exists('images'):
        os.makedirs('images')

    maze_file = sys.argv[1]
    maze = Maze("mazes/"+maze_file)
    print("Maze:")
    maze.print()
    print("Solving...")
    maze.solve()
    print("States Explored:", maze.num_explored)
    print("Solution:")
    maze.print()
    maze.output_image(maze_file.replace(".txt", ".png"), show_explored=True)
