# maze.py
import msvcrt
from inventory import pick_up_item, show_inventory  # Import functions from the inventory module
from combat import main
from maze_exit import end_game
from room_generation import *

# Define the player’s position and the grid (20x20) might need to be larger
GRID_SIZE = 42
player_position = [1, 1]  # Example starting position in the maze

# Sample maze structure with different types of cells
maze = [
    [{"type": "wall"}] * GRID_SIZE for _ in range(GRID_SIZE)
    # if the cell is not in the map below then it is defined as a wall
]

# THIS IS THE MAP
# Top Border #
maze[1][1] = {"type": "wall", "description": "It's a wall"}
maze[1][2] = {"type": "wall", "description": "It's a wall"}
maze[1][3] = {"type": "wall", "description": "It's a wall"}
maze[1][4] = {"type": "wall", "description": "It's a wall"}
maze[1][5] = {"type": "wall", "description": "It's a wall"}
maze[1][6] = {"type": "wall", "description": "It's a wall"}
maze[1][7] = {"type": "wall", "description": "It's a wall"}
maze[1][8] = {"type": "wall", "description": "It's a wall"}
maze[1][9] = {"type": "wall", "description": "It's a wall"}
maze[1][10] = {"type": "wall", "description": "It's a wall"}
maze[1][11] = {"type": "wall", "description": "It's a wall"}
maze[1][12] = {"type": "wall", "description": "It's a wall"}
maze[1][13] = {"type": "wall", "description": "It's a wall"}
maze[1][14] = {"type": "wall", "description": "It's a wall"}
maze[1][15] = {"type": "wall", "description": "It's a wall"}
maze[1][16] = {"type": "wall", "description": "It's a wall"}
maze[1][17] = {"type": "wall", "description": "It's a wall"}
maze[1][18] = {"type": "wall", "description": "It's a wall"}
maze[1][19] = {"type": "wall", "description": "It's a wall"}
maze[1][20] = {"type": "wall", "description": "It's a wall"}
maze[1][21] = {"type": "wall", "description": "It's a wall"}
maze[1][22] = {"type": "wall", "description": "It's a wall"}
maze[1][23] = {"type": "wall", "description": "It's a wall"}
maze[1][24] = {"type": "wall", "description": "It's a wall"}
maze[1][25] = {"type": "wall", "description": "It's a wall"}
maze[1][26] = {"type": "wall", "description": "It's a wall"}
maze[1][27] = {"type": "wall", "description": "It's a wall"}
maze[1][28] = {"type": "wall", "description": "It's a wall"}
maze[1][29] = {"type": "wall", "description": "It's a wall"}
maze[1][30] = {"type": "wall", "description": "It's a wall"}
maze[1][31] = {"type": "wall", "description": "It's a wall"}
maze[1][32] = {"type": "wall", "description": "It's a wall"}
maze[1][33] = {"type": "wall", "description": "It's a wall"}
maze[1][34] = {"type": "wall", "description": "It's a wall"}
maze[1][35] = {"type": "wall", "description": "It's a wall"}
maze[1][36] = {"type": "wall", "description": "It's a wall"}
maze[1][37] = {"type": "wall", "description": "It's a wall"}
maze[1][38] = {"type": "wall", "description": "It's a wall"}
maze[1][39] = {"type": "wall", "description": "It's a wall"}
maze[1][40] = {"type": "wall", "description": "It's a wall"}
maze[1][41] = {"type": "wall", "description": "It's a wall"}

# Bottom Border #
maze[41][1] = {"type": "wall", "description": "It's a wall"}
maze[41][2] = {"type": "wall", "description": "It's a wall"}
maze[41][3] = {"type": "wall", "description": "It's a wall"}
maze[41][4] = {"type": "wall", "description": "It's a wall"}
maze[41][5] = {"type": "wall", "description": "It's a wall"}
maze[41][6] = {"type": "wall", "description": "It's a wall"}
maze[41][7] = {"type": "wall", "description": "It's a wall"}
maze[41][8] = {"type": "wall", "description": "It's a wall"}
maze[41][9] = {"type": "wall", "description": "It's a wall"}
maze[41][10] = {"type": "wall", "description": "It's a wall"}
maze[41][11] = {"type": "wall", "description": "It's a wall"}
maze[41][12] = {"type": "wall", "description": "It's a wall"}
maze[41][13] = {"type": "wall", "description": "It's a wall"}
maze[41][14] = {"type": "wall", "description": "It's a wall"}
maze[41][15] = {"type": "wall", "description": "It's a wall"}
maze[41][16] = {"type": "wall", "description": "It's a wall"}
maze[41][17] = {"type": "wall", "description": "It's a wall"}
maze[41][18] = {"type": "wall", "description": "It's a wall"}
maze[41][19] = {"type": "wall", "description": "It's a wall"}
maze[41][20] = {"type": "wall", "description": "It's a wall"}
maze[41][21] = {"type": "wall", "description": "It's a wall"}
maze[41][22] = {"type": "wall", "description": "It's a wall"}
maze[41][23] = {"type": "wall", "description": "It's a wall"}
maze[41][24] = {"type": "wall", "description": "It's a wall"}
maze[41][25] = {"type": "wall", "description": "It's a wall"}
maze[41][26] = {"type": "wall", "description": "It's a wall"}
maze[41][27] = {"type": "wall", "description": "It's a wall"}
maze[41][28] = {"type": "wall", "description": "It's a wall"}
maze[41][29] = {"type": "wall", "description": "It's a wall"}
maze[41][30] = {"type": "wall", "description": "It's a wall"}
maze[41][31] = {"type": "wall", "description": "It's a wall"}
maze[41][32] = {"type": "wall", "description": "It's a wall"}
maze[41][33] = {"type": "wall", "description": "It's a wall"}
maze[41][34] = {"type": "wall", "description": "It's a wall"}
maze[41][35] = {"type": "wall", "description": "It's a wall"}
maze[41][36] = {"type": "wall", "description": "It's a wall"}
maze[41][37] = {"type": "wall", "description": "It's a wall"}
maze[41][38] = {"type": "wall", "description": "It's a wall"}
maze[41][39] = {"type": "wall", "description": "It's a wall"}
maze[41][40] = {"type": "wall", "description": "It's a wall"}
maze[41][41] = {"type": "wall", "description": "It's a wall"}

# Left Border #
maze[2][1] = {"type": "wall", "description": "It's a wall"}
maze[3][1] = {"type": "wall", "description": "It's a wall"}
maze[4][1] = {"type": "wall", "description": "It's a wall"}
maze[5][1] = {"type": "wall", "description": "It's a wall"}
maze[6][1] = {"type": "wall", "description": "It's a wall"}
maze[7][1] = {"type": "wall", "description": "It's a wall"}
maze[8][1] = {"type": "wall", "description": "It's a wall"}
maze[9][1] = {"type": "wall", "description": "It's a wall"}
maze[10][1] = {"type": "wall", "description": "It's a wall"}
maze[11][1] = {"type": "wall", "description": "It's a wall"}
maze[12][1] = {"type": "wall", "description": "It's a wall"}
maze[13][1] = {"type": "wall", "description": "It's a wall"}
maze[14][1] = {"type": "wall", "description": "It's a wall"}
maze[15][1] = {"type": "wall", "description": "It's a wall"}
maze[16][1] = {"type": "wall", "description": "It's a wall"}
maze[17][1] = {"type": "wall", "description": "It's a wall"}
maze[18][1] = {"type": "wall", "description": "It's a wall"}
maze[19][1] = {"type": "wall", "description": "It's a wall"}
maze[20][1] = {"type": "wall", "description": "It's a wall"}
maze[21][1] = {"type": "wall", "description": "It's a wall"}
maze[22][1] = {"type": "wall", "description": "It's a wall"}
maze[23][1] = {"type": "wall", "description": "It's a wall"}
maze[24][1] = {"type": "wall", "description": "It's a wall"}
maze[25][1] = {"type": "wall", "description": "It's a wall"}
maze[26][1] = {"type": "wall", "description": "It's a wall"}
maze[27][1] = {"type": "wall", "description": "It's a wall"}
maze[28][1] = {"type": "wall", "description": "It's a wall"}
maze[29][1] = {"type": "wall", "description": "It's a wall"}
maze[30][1] = {"type": "wall", "description": "It's a wall"}
maze[31][1] = {"type": "wall", "description": "It's a wall"}
maze[32][1] = {"type": "wall", "description": "It's a wall"}
maze[33][1] = {"type": "wall", "description": "It's a wall"}
maze[34][1] = {"type": "wall", "description": "It's a wall"}
maze[35][1] = {"type": "wall", "description": "It's a wall"}
maze[36][1] = {"type": "wall", "description": "It's a wall"}
maze[37][1] = {"type": "wall", "description": "It's a wall"}
maze[38][1] = {"type": "wall", "description": "It's a wall"}
maze[39][1] = {"type": "wall", "description": "It's a wall"}
maze[40][1] = {"type": "wall", "description": "It's a wall"}

# Right Border #
maze[2][41] = {"type": "wall", "description": "It's a wall"}
maze[3][41] = {"type": "wall", "description": "It's a wall"}
maze[4][41] = {"type": "wall", "description": "It's a wall"}
maze[5][41] = {"type": "wall", "description": "It's a wall"}
maze[6][41] = {"type": "wall", "description": "It's a wall"}
maze[7][41] = {"type": "wall", "description": "It's a wall"}
maze[8][41] = {"type": "wall", "description": "It's a wall"}
maze[9][41] = {"type": "wall", "description": "It's a wall"}
maze[10][41] = {"type": "wall", "description": "It's a wall"}
maze[11][41] = {"type": "wall", "description": "It's a wall"}
maze[12][41] = {"type": "wall", "description": "It's a wall"}
maze[13][41] = {"type": "wall", "description": "It's a wall"}
maze[14][41] = {"type": "wall", "description": "It's a wall"}
maze[15][41] = {"type": "wall", "description": "It's a wall"}
maze[16][41] = {"type": "wall", "description": "It's a wall"}
maze[17][41] = {"type": "wall", "description": "It's a wall"}
maze[18][41] = {"type": "wall", "description": "It's a wall"}
maze[19][41] = {"type": "wall", "description": "It's a wall"}
maze[20][41] = {"type": "wall", "description": "It's a wall"}
maze[21][41] = {"type": "wall", "description": "It's a wall"}
maze[22][41] = {"type": "wall", "description": "It's a wall"}
maze[23][41] = {"type": "wall", "description": "It's a wall"}
maze[24][41] = {"type": "wall", "description": "It's a wall"}
maze[25][41] = {"type": "wall", "description": "It's a wall"}
maze[26][41] = {"type": "wall", "description": "It's a wall"}
maze[27][41] = {"type": "wall", "description": "It's a wall"}
maze[28][41] = {"type": "wall", "description": "It's a wall"}
maze[29][41] = {"type": "wall", "description": "It's a wall"}
maze[30][41] = {"type": "wall", "description": "It's a wall"}
maze[31][41] = {"type": "wall", "description": "It's a wall"}
maze[32][41] = {"type": "wall", "description": "It's a wall"}
maze[33][41] = {"type": "wall", "description": "It's a wall"}
maze[34][41] = {"type": "wall", "description": "It's a wall"}
maze[35][41] = {"type": "wall", "description": "It's a wall"}
maze[36][41] = {"type": "wall", "description": "It's a wall"}
maze[37][41] = {"type": "wall", "description": "It's a wall"}
maze[38][41] = {"type": "wall", "description": "It's a wall"}
maze[39][41] = {"type": "wall", "description": "It's a wall"}
maze[40][41] = {"type": "wall", "description": "It's a wall"}

# Starting Point #
maze[2][2] = {"type": "start", "description": "Starting Location"}

# Hallways #
# Row 2 #
maze[2][3] = {"type": "hall", "description": "A long dark hall"}
maze[2][4] = {"type": "hall", "description": "A long dark hall"}
maze[2][5] = {"type": "hall", "description": "A long dark hall"}
maze[2][6] = {"type": "hall", "description": "A long dark hall"}
maze[2][7] = {"type": "hall", "description": "A long dark hall"}
maze[2][6] = {"type": "hall", "description": "A long dark hall"}
maze[2][7] = {"type": "hall", "description": "A long dark hall"}
maze[2][8] = {"type": "hall", "description": "A long dark hall"}
maze[2][9] = {"type": "hall", "description": "A long dark hall"}
maze[2][10] = {"type": "hall", "description": "A long dark hall"}
maze[2][11] = {"type": "hall", "description": "A long dark hall"}
maze[2][12] = {"type": "hall", "description": "A long dark hall"}
maze[2][13] = {"type": "hall", "description": "A long dark hall"}
maze[2][14] = {"type": "hall", "description": "A long dark hall"}
maze[2][15] = {"type": "hall", "description": "A long dark hall"}
maze[2][16] = {"type": "hall", "description": "A long dark hall"}
maze[2][17] = {"type": "hall", "description": "A long dark hall"}
maze[2][18] = {"type": "hall", "description": "A long dark hall"}
maze[2][19] = {"type": "hall", "description": "A long dark hall"}
maze[2][20] = {"type": "hall", "description": "A long dark hall"}
maze[2][21] = {"type": "hall", "description": "A long dark hall"}
maze[2][22] = {"type": "hall", "description": "A long dark hall"}
maze[2][23] = {"type": "hall", "description": "A long dark hall"}
maze[2][24] = {"type": "hall", "description": "A long dark hall"}
maze[2][25] = {"type": "hall", "description": "A long dark hall"}
maze[2][26] = {"type": "hall", "description": "A long dark hall"}
maze[2][27] = {"type": "hall", "description": "A long dark hall"}
maze[2][28] = {"type": "hall", "description": "A long dark hall"}
maze[2][29] = {"type": "hall", "description": "A long dark hall"}
maze[2][30] = {"type": "hall", "description": "A long dark hall"}
maze[2][31] = {"type": "hall", "description": "A long dark hall"}
maze[2][32] = {"type": "hall", "description": "A long dark hall"}
maze[2][33] = {"type": "hall", "description": "A long dark hall"}
maze[2][34] = {"type": "hall", "description": "A long dark hall"}
maze[2][35] = {"type": "hall", "description": "A long dark hall"}
maze[2][36] = {"type": "hall", "description": "A long dark hall"}
maze[2][37] = {"type": "hall", "description": "A long dark hall"}
maze[2][38] = {"type": "hall", "description": "A long dark hall"}
maze[2][39] = {"type": "hall", "description": "A long dark hall"}
maze[2][40] = {"type": "hall", "description": "A long dark hall"}

# Row 3 #
maze[3][2] = {"type": "hall", "description": "A long dark hall"}
maze[3][22] = {"type": "hall", "description": "A long dark hall"}
maze[3][40] = {"type": "hall", "description": "A long dark hall"}

# Row 4 #
maze[4][2] = {"type": "hall", "description": "A long dark hall"}
maze[4][4] = {"type": "hall", "description": "A long dark hall"}
maze[4][5] = {"type": "hall", "description": "A long dark hall"}
maze[4][6] = {"type": "hall", "description": "A long dark hall"}
maze[4][7] = {"type": "hall", "description": "A long dark hall"}
maze[4][8] = {"type": "hall", "description": "A long dark hall"}
maze[4][9] = {"type": "hall", "description": "A long dark hall"}
maze[4][10] = {"type": "hall", "description": "A long dark hall"}
maze[4][11] = {"type": "hall", "description": "A long dark hall"}
maze[4][12] = {"type": "hall", "description": "A long dark hall"}
maze[4][13] = {"type": "hall", "description": "A long dark hall"}
maze[4][14] = {"type": "hall", "description": "A long dark hall"}
maze[4][15] = {"type": "hall", "description": "A long dark hall"}
maze[4][16] = {"type": "hall", "description": "A long dark hall"}
maze[4][17] = {"type": "hall", "description": "A long dark hall"}
maze[4][18] = {"type": "hall", "description": "A long dark hall"}
maze[4][19] = {"type": "hall", "description": "A long dark hall"}
maze[4][20] = {"type": "hall", "description": "A long dark hall"}
maze[4][21] = {"type": "hall", "description": "A long dark hall"}
maze[4][22] = {"type": "hall", "description": "A long dark hall"}
maze[4][23] = {"type": "hall", "description": "A long dark hall"}
maze[4][24] = {"type": "hall", "description": "A long dark hall"}
maze[4][25] = {"type": "hall", "description": "A long dark hall"}
maze[4][26] = {"type": "hall", "description": "A long dark hall"}
maze[4][27] = {"type": "hall", "description": "A long dark hall"}
maze[4][28] = {"type": "hall", "description": "A long dark hall"}
maze[4][29] = {"type": "hall", "description": "A long dark hall"}
maze[4][30] = {"type": "hall", "description": "A long dark hall"}
maze[4][31] = {"type": "hall", "description": "A long dark hall"}
maze[4][32] = {"type": "hall", "description": "A long dark hall"}
maze[4][33] = {"type": "hall", "description": "A long dark hall"}
maze[4][34] = {"type": "hall", "description": "A long dark hall"}
maze[4][35] = {"type": "hall", "description": "A long dark hall"}
maze[4][36] = {"type": "hall", "description": "A long dark hall"}
maze[4][37] = {"type": "hall", "description": "A long dark hall"}
maze[4][38] = {"type": "hall", "description": "A long dark hall"}
maze[4][40] = {"type": "hall", "description": "A long dark hall"}

# Row 5 #
maze[5][2] = {"type": "hall", "description": "A long dark hall"}
maze[5][4] = {"type": "hall", "description": "A long dark hall"}
maze[5][20] = {"type": "hall", "description": "A long dark hall"}
maze[5][24] = {"type": "hall", "description": "A long dark hall"}
maze[5][38] = {"type": "hall", "description": "A long dark hall"}
maze[5][40] = {"type": "hall", "description": "A long dark hall"}

# Row 6 #
maze[6][2] = {"type": "hall", "description": "A long dark hall"}
maze[6][4] = {"type": "hall", "description": "A long dark hall"}
maze[6][10] = {"type": "hall", "description": "A long dark hall"}
maze[6][11] = {"type": "hall", "description": "A long dark hall"}
maze[6][12] = {"type": "hall", "description": "A long dark hall"}
maze[6][13] = {"type": "hall", "description": "A long dark hall"}
maze[6][14] = {"type": "hall", "description": "A long dark hall"}
maze[6][15] = {"type": "hall", "description": "A long dark hall"}
maze[6][16] = {"type": "hall", "description": "A long dark hall"}
maze[6][17] = {"type": "hall", "description": "A long dark hall"}
maze[6][18] = {"type": "hall", "description": "A long dark hall"}
maze[6][20] = {"type": "hall", "description": "A long dark hall"}
maze[6][22] = {"type": "hall", "description": "A long dark hall"}
maze[6][23] = {"type": "hall", "description": "A long dark hall"}
maze[6][24] = {"type": "hall", "description": "A long dark hall"}
maze[6][25] = {"type": "hall", "description": "A long dark hall"}
maze[6][26] = {"type": "hall", "description": "A long dark hall"}
maze[6][27] = {"type": "hall", "description": "A long dark hall"}
maze[6][28] = {"type": "hall", "description": "A long dark hall"}
maze[6][29] = {"type": "hall", "description": "A long dark hall"}
maze[6][30] = {"type": "hall", "description": "A long dark hall"}
maze[6][31] = {"type": "hall", "description": "A long dark hall"}
maze[6][32] = {"type": "hall", "description": "A long dark hall"}
maze[6][33] = {"type": "hall", "description": "A long dark hall"}
maze[6][34] = {"type": "hall", "description": "A long dark hall"}
maze[6][35] = {"type": "hall", "description": "A long dark hall"}
maze[6][36] = {"type": "hall", "description": "A long dark hall"}
maze[6][38] = {"type": "hall", "description": "A long dark hall"}
maze[6][40] = {"type": "hall", "description": "A long dark hall"}

# Row 7 #
maze[7][2] = {"type": "hall", "description": "A long dark hall"}
maze[7][4] = {"type": "hall", "description": "A long dark hall"}
maze[7][10] = {"type": "hall", "description": "A long dark hall"}
maze[7][18] = {"type": "hall", "description": "A long dark hall"}
maze[7][20] = {"type": "hall", "description": "A long dark hall"}
maze[7][22] = {"type": "hall", "description": "A long dark hall"}
maze[7][36] = {"type": "hall", "description": "A long dark hall"}
maze[7][38] = {"type": "hall", "description": "A long dark hall"}
maze[7][40] = {"type": "hall", "description": "A long dark hall"}

# Row 8 #
maze[8][2] = {"type": "hall", "description": "A long dark hall"}
maze[8][4] = {"type": "hall", "description": "A long dark hall"}
maze[8][10] = {"type": "hall", "description": "A long dark hall"}
maze[8][18] = {"type": "hall", "description": "A long dark hall"}
maze[8][19] = {"type": "hall", "description": "A long dark hall"}
maze[8][20] = {"type": "hall", "description": "A long dark hall"}
maze[8][22] = {"type": "hall", "description": "A long dark hall"}
maze[8][24] = {"type": "hall", "description": "A long dark hall"}
maze[8][25] = {"type": "hall", "description": "A long dark hall"}
maze[8][26] = {"type": "hall", "description": "A long dark hall"}
maze[8][27] = {"type": "hall", "description": "A long dark hall"}
maze[8][28] = {"type": "hall", "description": "A long dark hall"}
maze[8][29] = {"type": "hall", "description": "A long dark hall"}
maze[8][30] = {"type": "hall", "description": "A long dark hall"}
maze[8][31] = {"type": "hall", "description": "A long dark hall"}
maze[8][32] = {"type": "hall", "description": "A long dark hall"}
maze[8][33] = {"type": "hall", "description": "A long dark hall"}
maze[8][34] = {"type": "hall", "description": "A long dark hall"}
maze[8][36] = {"type": "hall", "description": "A long dark hall"}
maze[8][38] = {"type": "hall", "description": "A long dark hall"}
maze[8][40] = {"type": "hall", "description": "A long dark hall"}

# Row 9 #
maze[9][2] = {"type": "hall", "description": "A long dark hall"}
maze[9][4] = {"type": "hall", "description": "A long dark hall"}
maze[9][10] = {"type": "hall", "description": "A long dark hall"}
maze[9][18] = {"type": "hall", "description": "A long dark hall"}
maze[9][20] = {"type": "hall", "description": "A long dark hall"}
maze[9][22] = {"type": "hall", "description": "A long dark hall"}
maze[9][24] = {"type": "hall", "description": "A long dark hall"}
maze[9][34] = {"type": "hall", "description": "A long dark hall"}
maze[9][36] = {"type": "hall", "description": "A long dark hall"}
maze[9][38] = {"type": "hall", "description": "A long dark hall"}
maze[9][40] = {"type": "hall", "description": "A long dark hall"}


# Row 10 #
maze[10][2] = {"type": "hall", "description": "A long dark hall"}
maze[10][4] = {"type": "hall", "description": "A long dark hall"}
maze[10][10] = {"type": "hall", "description": "A long dark hall"}
maze[10][11] = {"type": "hall", "description": "A long dark hall"}
maze[10][18] = {"type": "hall", "description": "A long dark hall"}
maze[10][20] = {"type": "hall", "description": "A long dark hall"}
maze[10][22] = {"type": "hall", "description": "A long dark hall"}
maze[10][23] = {"type": "hall", "description": "A long dark hall"}
maze[10][24] = {"type": "hall", "description": "A long dark hall"}
maze[10][34] = {"type": "hall", "description": "A long dark hall"}
maze[10][36] = {"type": "hall", "description": "A long dark hall"}
maze[10][38] = {"type": "hall", "description": "A long dark hall"}
maze[10][40] = {"type": "hall", "description": "A long dark hall"}


# Row 11 #
maze[11][2] = {"type": "hall", "description": "A long dark hall"}
maze[11][4] = {"type": "hall", "description": "A long dark hall"}
maze[11][10] = {"type": "hall", "description": "A long dark hall"}
maze[11][18] = {"type": "hall", "description": "A long dark hall"}
maze[11][20] = {"type": "hall", "description": "A long dark hall"}
maze[11][22] = {"type": "hall", "description": "A long dark hall"}
maze[11][24] = {"type": "hall", "description": "A long dark hall"}
maze[11][34] = {"type": "hall", "description": "A long dark hall"}
maze[11][36] = {"type": "hall", "description": "A long dark hall"}
maze[11][38] = {"type": "hall", "description": "A long dark hall"}
maze[11][40] = {"type": "hall", "description": "A long dark hall"}

# Row 12 #
maze[12][2] = {"type": "hall", "description": "A long dark hall"}
maze[12][4] = {"type": "hall", "description": "A long dark hall"}
maze[12][10] = {"type": "hall", "description": "A long dark hall"}
maze[12][18] = {"type": "hall", "description": "A long dark hall"}
maze[12][20] = {"type": "hall", "description": "A long dark hall"}
maze[12][22] = {"type": "hall", "description": "A long dark hall"}
maze[12][24] = {"type": "hall", "description": "A long dark hall"}
maze[12][34] = {"type": "hall", "description": "A long dark hall"}
maze[12][36] = {"type": "hall", "description": "A long dark hall"}
maze[12][38] = {"type": "hall", "description": "A long dark hall"}
maze[12][40] = {"type": "hall", "description": "A long dark hall"}

# Row 13 #
maze[13][2] = {"type": "hall", "description": "A long dark hall"}
maze[13][4] = {"type": "hall", "description": "A long dark hall"}
maze[13][10] = {"type": "hall", "description": "A long dark hall"}
maze[13][18] = {"type": "hall", "description": "A long dark hall"}
maze[13][20] = {"type": "hall", "description": "A long dark hall"}
maze[13][22] = {"type": "hall", "description": "A long dark hall"}
maze[13][24] = {"type": "hall", "description": "A long dark hall"}
maze[13][34] = {"type": "hall", "description": "A long dark hall"}
maze[13][36] = {"type": "hall", "description": "A long dark hall"}
maze[13][38] = {"type": "hall", "description": "A long dark hall"}
maze[13][40] = {"type": "hall", "description": "A long dark hall"}

# Row 14 #
maze[14][2] = {"type": "hall", "description": "A long dark hall"}
maze[14][4] = {"type": "hall", "description": "A long dark hall"}
maze[14][10] = {"type": "hall", "description": "A long dark hall"}
maze[14][11] = {"type": "hall", "description": "A long dark hall"}
maze[14][12] = {"type": "hall", "description": "A long dark hall"}
maze[14][13] = {"type": "hall", "description": "A long dark hall"}
maze[14][14] = {"type": "hall", "description": "A long dark hall"}
maze[14][15] = {"type": "hall", "description": "A long dark hall"}
maze[14][16] = {"type": "hall", "description": "A long dark hall"}
maze[14][17] = {"type": "hall", "description": "A long dark hall"}
maze[14][18] = {"type": "hall", "description": "A long dark hall"}
maze[14][20] = {"type": "hall", "description": "A long dark hall"}
maze[14][22] = {"type": "hall", "description": "A long dark hall"}
maze[14][24] = {"type": "hall", "description": "A long dark hall"}
maze[14][25] = {"type": "hall", "description": "A long dark hall"}
maze[14][34] = {"type": "hall", "description": "A long dark hall"}
maze[14][36] = {"type": "hall", "description": "A long dark hall"}
maze[14][37] = {"type": "hall", "description": "A long dark hall"}
maze[14][38] = {"type": "hall", "description": "A long dark hall"}
maze[14][40] = {"type": "hall", "description": "A long dark hall"}

# Row 15 #
maze[15][2] = {"type": "hall", "description": "A long dark hall"}
maze[15][4] = {"type": "hall", "description": "A long dark hall"}
maze[15][20] = {"type": "hall", "description": "A long dark hall"}
maze[15][22] = {"type": "hall", "description": "A long dark hall"}
maze[15][24] = {"type": "hall", "description": "A long dark hall"}
maze[15][34] = {"type": "hall", "description": "A long dark hall"}
maze[15][36] = {"type": "hall", "description": "A long dark hall"}
maze[15][38] = {"type": "hall", "description": "A long dark hall"}
maze[15][40] = {"type": "hall", "description": "A long dark hall"}

# Row 16 #
maze[16][2] = {"type": "hall", "description": "A long dark hall"}
maze[16][4] = {"type": "hall", "description": "A long dark hall"}
maze[16][5] = {"type": "hall", "description": "A long dark hall"}
maze[16][6] = {"type": "hall", "description": "A long dark hall"}
maze[16][7] = {"type": "hall", "description": "A long dark hall"}
maze[16][8] = {"type": "hall", "description": "A long dark hall"}
maze[16][9] = {"type": "hall", "description": "A long dark hall"}
maze[16][10] = {"type": "hall", "description": "A long dark hall"}
maze[16][11] = {"type": "hall", "description": "A long dark hall"}
maze[16][12] = {"type": "hall", "description": "A long dark hall"}
maze[16][13] = {"type": "hall", "description": "A long dark hall"}
maze[16][14] = {"type": "hall", "description": "A long dark hall"}
maze[16][15] = {"type": "hall", "description": "A long dark hall"}
maze[16][16] = {"type": "hall", "description": "A long dark hall"}
maze[16][17] = {"type": "hall", "description": "A long dark hall"}
maze[16][18] = {"type": "hall", "description": "A long dark hall"}
maze[16][19] = {"type": "hall", "description": "A long dark hall"}
maze[16][20] = {"type": "hall", "description": "A long dark hall"}
maze[16][22] = {"type": "hall", "description": "A long dark hall"}
maze[16][24] = {"type": "hall", "description": "A long dark hall"}
maze[16][34] = {"type": "hall", "description": "A long dark hall"}
maze[16][36] = {"type": "hall", "description": "A long dark hall"}
maze[16][38] = {"type": "hall", "description": "A long dark hall"}
maze[16][40] = {"type": "hall", "description": "A long dark hall"}

# Row 17 #
maze[17][2] = {"type": "hall", "description": "A long dark hall"}
maze[17][4] = {"type": "hall", "description": "A long dark hall"}
maze[17][20] = {"type": "hall", "description": "A long dark hall"}
maze[17][22] = {"type": "hall", "description": "A long dark hall"}
maze[17][24] = {"type": "hall", "description": "A long dark hall"}
maze[17][34] = {"type": "hall", "description": "A long dark hall"}
maze[17][36] = {"type": "hall", "description": "A long dark hall"}
maze[17][38] = {"type": "hall", "description": "A long dark hall"}
maze[17][40] = {"type": "hall", "description": "A long dark hall"}

# Row 18 #
maze[18][2] = {"type": "hall", "description": "A long dark hall"}
maze[18][4] = {"type": "hall", "description": "A long dark hall"}
maze[18][20] = {"type": "hall", "description": "A long dark hall"}
maze[18][22] = {"type": "hall", "description": "A long dark hall"}
maze[18][24] = {"type": "hall", "description": "A long dark hall"}
maze[18][25] = {"type": "hall", "description": "A long dark hall"}
maze[18][26] = {"type": "hall", "description": "A long dark hall"}
maze[18][27] = {"type": "hall", "description": "A long dark hall"}
maze[18][28] = {"type": "hall", "description": "A long dark hall"}
maze[18][29] = {"type": "hall", "description": "A long dark hall"}
maze[18][30] = {"type": "hall", "description": "A long dark hall"}
maze[18][31] = {"type": "hall", "description": "A long dark hall"}
maze[18][32] = {"type": "hall", "description": "A long dark hall"}
maze[18][33] = {"type": "hall", "description": "A long dark hall"}
maze[18][34] = {"type": "hall", "description": "A long dark hall"}
maze[18][36] = {"type": "hall", "description": "A long dark hall"}
maze[18][38] = {"type": "hall", "description": "A long dark hall"}
maze[18][40] = {"type": "hall", "description": "A long dark hall"}

# Row 19 #
maze[19][2] = {"type": "hall", "description": "A long dark hall"}
maze[19][4] = {"type": "hall", "description": "A long dark hall"}
maze[19][20] = {"type": "hall", "description": "A long dark hall"}
maze[19][22] = {"type": "hall", "description": "A long dark hall"}
maze[19][32] = {"type": "hall", "description": "A long dark hall"}
maze[19][36] = {"type": "hall", "description": "A long dark hall"}
maze[19][38] = {"type": "hall", "description": "A long dark hall"}
maze[19][40] = {"type": "hall", "description": "A long dark hall"}

# Row 20 #
maze[20][2] = {"type": "hall", "description": "A long dark hall"}
maze[20][4] = {"type": "hall", "description": "A long dark hall"}
maze[20][20] = {"type": "hall", "description": "A long dark hall"}
maze[20][22] = {"type": "hall", "description": "A long dark hall"}
maze[20][23] = {"type": "hall", "description": "A long dark hall"}
maze[20][24] = {"type": "hall", "description": "A long dark hall"}
maze[20][25] = {"type": "hall", "description": "A long dark hall"}
maze[20][26] = {"type": "hall", "description": "A long dark hall"}
maze[20][27] = {"type": "hall", "description": "A long dark hall"}
maze[20][28] = {"type": "hall", "description": "A long dark hall"}
maze[20][29] = {"type": "hall", "description": "A long dark hall"}
maze[20][30] = {"type": "hall", "description": "A long dark hall"}
maze[20][31] = {"type": "hall", "description": "A long dark hall"}
maze[20][32] = {"type": "hall", "description": "A long dark hall"}
maze[20][33] = {"type": "hall", "description": "A long dark hall"}
maze[20][34] = {"type": "hall", "description": "A long dark hall"}
maze[20][35] = {"type": "hall", "description": "A long dark hall"}
maze[20][36] = {"type": "hall", "description": "A long dark hall"}
maze[20][38] = {"type": "hall", "description": "A long dark hall"}
maze[20][40] = {"type": "hall", "description": "A long dark hall"}

# Row 21 #
maze[21][2] = {"type": "hall", "description": "A long dark hall"}
maze[21][4] = {"type": "hall", "description": "A long dark hall"}
maze[21][12] = {"type": "hall", "description": "A long dark hall"}
maze[21][20] = {"type": "hall", "description": "A long dark hall"}
maze[21][24] = {"type": "hall", "description": "A long dark hall"}
maze[21][36] = {"type": "hall", "description": "A long dark hall"}
maze[21][38] = {"type": "hall", "description": "A long dark hall"}
maze[21][40] = {"type": "hall", "description": "A long dark hall"}

# Row 22 #
maze[22][2] = {"type": "hall", "description": "A long dark hall"}
maze[22][4] = {"type": "hall", "description": "A long dark hall"}
maze[22][5] = {"type": "hall", "description": "A long dark hall"}
maze[22][6] = {"type": "hall", "description": "A long dark hall"}
maze[22][7] = {"type": "hall", "description": "A long dark hall"}
maze[22][8] = {"type": "hall", "description": "A long dark hall"}
maze[22][9] = {"type": "hall", "description": "A long dark hall"}
maze[22][10] = {"type": "hall", "description": "A long dark hall"}
maze[22][11] = {"type": "hall", "description": "A long dark hall"}
maze[22][12] = {"type": "hall", "description": "A long dark hall"}
maze[22][13] = {"type": "hall", "description": "A long dark hall"}
maze[22][14] = {"type": "hall", "description": "A long dark hall"}
maze[22][15] = {"type": "hall", "description": "A long dark hall"}
maze[22][16] = {"type": "hall", "description": "A long dark hall"}
maze[22][17] = {"type": "hall", "description": "A long dark hall"}
maze[22][18] = {"type": "hall", "description": "A long dark hall"}
maze[22][19] = {"type": "hall", "description": "A long dark hall"}
maze[22][20] = {"type": "hall", "description": "A long dark hall"}
maze[22][21] = {"type": "hall", "description": "A long dark hall"}
maze[22][22] = {"type": "hall", "description": "A long dark hall"}
maze[22][23] = {"type": "hall", "description": "A long dark hall"}
maze[22][24] = {"type": "hall", "description": "A long dark hall"}
maze[22][25] = {"type": "hall", "description": "A long dark hall"}
maze[22][26] = {"type": "hall", "description": "A long dark hall"}
maze[22][27] = {"type": "hall", "description": "A long dark hall"}
maze[22][28] = {"type": "hall", "description": "A long dark hall"}
maze[22][29] = {"type": "hall", "description": "A long dark hall"}
maze[22][30] = {"type": "hall", "description": "A long dark hall"}
maze[22][31] = {"type": "hall", "description": "A long dark hall"}
maze[22][32] = {"type": "hall", "description": "A long dark hall"}
maze[22][33] = {"type": "hall", "description": "A long dark hall"}
maze[22][34] = {"type": "hall", "description": "A long dark hall"}
maze[22][35] = {"type": "hall", "description": "A long dark hall"}
maze[22][36] = {"type": "hall", "description": "A long dark hall"}
maze[22][37] = {"type": "hall", "description": "A long dark hall"}
maze[22][38] = {"type": "hall", "description": "A long dark hall"}
maze[22][40] = {"type": "hall", "description": "A long dark hall"}

# Row 23 #
maze[23][2] = {"type": "hall", "description": "A long dark hall"}
maze[23][4] = {"type": "hall", "description": "A long dark hall"}
maze[23][30] = {"type": "hall", "description": "A long dark hall"}
maze[23][38] = {"type": "hall", "description": "A long dark hall"}
maze[23][40] = {"type": "hall", "description": "A long dark hall"}

# Row 24 #
maze[24][2] = {"type": "hall", "description": "A long dark hall"}
maze[24][3] = {"type": "hall", "description": "A long dark hall"}
maze[24][4] = {"type": "hall", "description": "A long dark hall"}
maze[24][6] = {"type": "hall", "description": "A long dark hall"}
maze[24][7] = {"type": "hall", "description": "A long dark hall"}
maze[24][8] = {"type": "hall", "description": "A long dark hall"}
maze[24][9] = {"type": "hall", "description": "A long dark hall"}
maze[24][10] = {"type": "hall", "description": "A long dark hall"}
maze[24][11] = {"type": "hall", "description": "A long dark hall"}
maze[24][12] = {"type": "hall", "description": "A long dark hall"}
maze[24][13] = {"type": "hall", "description": "A long dark hall"}
maze[24][14] = {"type": "hall", "description": "A long dark hall"}
maze[24][15] = {"type": "hall", "description": "A long dark hall"}
maze[24][16] = {"type": "hall", "description": "A long dark hall"}
maze[24][17] = {"type": "hall", "description": "A long dark hall"}
maze[24][18] = {"type": "hall", "description": "A long dark hall"}
maze[24][19] = {"type": "hall", "description": "A long dark hall"}
maze[24][20] = {"type": "hall", "description": "A long dark hall"}
maze[24][21] = {"type": "hall", "description": "A long dark hall"}
maze[24][22] = {"type": "hall", "description": "A long dark hall"}
maze[24][23] = {"type": "hall", "description": "A long dark hall"}
maze[24][24] = {"type": "hall", "description": "A long dark hall"}
maze[24][25] = {"type": "hall", "description": "A long dark hall"}
maze[24][26] = {"type": "hall", "description": "A long dark hall"}
maze[24][27] = {"type": "hall", "description": "A long dark hall"}
maze[24][28] = {"type": "hall", "description": "A long dark hall"}
maze[24][29] = {"type": "hall", "description": "A long dark hall"}
maze[24][30] = {"type": "hall", "description": "A long dark hall"}
maze[24][31] = {"type": "hall", "description": "A long dark hall"}
maze[24][32] = {"type": "hall", "description": "A long dark hall"}
maze[24][33] = {"type": "hall", "description": "A long dark hall"}
maze[24][34] = {"type": "hall", "description": "A long dark hall"}
maze[24][35] = {"type": "hall", "description": "A long dark hall"}
maze[24][36] = {"type": "hall", "description": "A long dark hall"}
maze[24][38] = {"type": "hall", "description": "A long dark hall"}
maze[24][40] = {"type": "hall", "description": "A long dark hall"}

# Row 25 #
maze[25][2] = {"type": "hall", "description": "A long dark hall"}
maze[25][4] = {"type": "hall", "description": "A long dark hall"}
maze[25][6] = {"type": "hall", "description": "A long dark hall"}
maze[25][12] = {"type": "hall", "description": "A long dark hall"}
maze[25][34] = {"type": "hall", "description": "A long dark hall"}
maze[25][35] = {"type": "hall", "description": "A long dark hall"}
maze[25][36] = {"type": "hall", "description": "A long dark hall"}
maze[25][38] = {"type": "hall", "description": "A long dark hall"}
maze[25][40] = {"type": "hall", "description": "A long dark hall"}

# Row 26 #
maze[26][2] = {"type": "hall", "description": "A long dark hall"}
maze[26][4] = {"type": "hall", "description": "A long dark hall"}
maze[26][6] = {"type": "hall", "description": "A long dark hall"}
maze[26][8] = {"type": "hall", "description": "A long dark hall"}
maze[26][9] = {"type": "hall", "description": "A long dark hall"}
maze[26][10] = {"type": "hall", "description": "A long dark hall"}
maze[26][11] = {"type": "hall", "description": "A long dark hall"}
maze[26][12] = {"type": "hall", "description": "A long dark hall"}
maze[26][13] = {"type": "hall", "description": "A long dark hall"}
maze[26][14] = {"type": "hall", "description": "A long dark hall"}
maze[26][15] = {"type": "hall", "description": "A long dark hall"}
maze[26][16] = {"type": "hall", "description": "A long dark hall"}
maze[26][17] = {"type": "hall", "description": "A long dark hall"}
maze[26][18] = {"type": "hall", "description": "A long dark hall"}
maze[26][19] = {"type": "hall", "description": "A long dark hall"}
maze[26][20] = {"type": "hall", "description": "A long dark hall"}
maze[26][21] = {"type": "hall", "description": "A long dark hall"}
maze[26][22] = {"type": "hall", "description": "A long dark hall"}
maze[26][23] = {"type": "hall", "description": "A long dark hall"}
maze[26][24] = {"type": "hall", "description": "A long dark hall"}
maze[26][25] = {"type": "hall", "description": "A long dark hall"}
maze[26][26] = {"type": "hall", "description": "A long dark hall"}
maze[26][27] = {"type": "hall", "description": "A long dark hall"}
maze[26][28] = {"type": "hall", "description": "A long dark hall"}
maze[26][29] = {"type": "hall", "description": "A long dark hall"}
maze[26][30] = {"type": "hall", "description": "A long dark hall"}
maze[26][31] = {"type": "hall", "description": "A long dark hall"}
maze[26][32] = {"type": "hall", "description": "A long dark hall"}
maze[26][34] = {"type": "hall", "description": "A long dark hall"}
maze[26][35] = {"type": "hall", "description": "A long dark hall"}
maze[26][36] = {"type": "hall", "description": "A long dark hall"}
maze[26][38] = {"type": "hall", "description": "A long dark hall"}
maze[26][40] = {"type": "hall", "description": "A long dark hall"}

# Row 27 #
maze[27][2] = {"type": "hall", "description": "A long dark hall"}
maze[27][4] = {"type": "hall", "description": "A long dark hall"}
maze[27][6] = {"type": "hall", "description": "A long dark hall"}
maze[27][8] = {"type": "hall", "description": "A long dark hall"}
maze[27][24] = {"type": "hall", "description": "A long dark hall"}
maze[27][32] = {"type": "hall", "description": "A long dark hall"}
maze[27][34] = {"type": "hall", "description": "A long dark hall"}
maze[27][35] = {"type": "hall", "description": "A long dark hall"}
maze[27][36] = {"type": "hall", "description": "A long dark hall"}
maze[27][38] = {"type": "hall", "description": "A long dark hall"}
maze[27][40] = {"type": "hall", "description": "A long dark hall"}

# Row 28 #
maze[28][2] = {"type": "hall", "description": "A long dark hall"}
maze[28][4] = {"type": "hall", "description": "A long dark hall"}
maze[28][6] = {"type": "hall", "description": "A long dark hall"}
maze[28][8] = {"type": "hall", "description": "A long dark hall"}
maze[28][24] = {"type": "hall", "description": "A long dark hall"}
maze[28][32] = {"type": "hall", "description": "A long dark hall"}
maze[28][34] = {"type": "hall", "description": "A long dark hall"}
maze[28][35] = {"type": "hall", "description": "A long dark hall"}
maze[28][36] = {"type": "hall", "description": "A long dark hall"}
maze[28][38] = {"type": "hall", "description": "A long dark hall"}
maze[28][40] = {"type": "hall", "description": "A long dark hall"}

# Row 29 #
maze[29][2] = {"type": "hall", "description": "A long dark hall"}
maze[29][4] = {"type": "hall", "description": "A long dark hall"}
maze[29][6] = {"type": "hall", "description": "A long dark hall"}
maze[29][8] = {"type": "hall", "description": "A long dark hall"}
maze[29][24] = {"type": "hall", "description": "A long dark hall"}
maze[29][32] = {"type": "hall", "description": "A long dark hall"}
maze[29][34] = {"type": "hall", "description": "A long dark hall"}
maze[29][35] = {"type": "hall", "description": "A long dark hall"}
maze[29][36] = {"type": "hall", "description": "A long dark hall"}
maze[29][38] = {"type": "hall", "description": "A long dark hall"}
maze[29][40] = {"type": "hall", "description": "A long dark hall"}

# Row 30 #
maze[30][2] = {"type": "hall", "description": "A long dark hall"}
maze[30][4] = {"type": "hall", "description": "A long dark hall"}
maze[30][6] = {"type": "hall", "description": "A long dark hall"}
maze[30][8] = {"type": "hall", "description": "A long dark hall"}
maze[30][24] = {"type": "hall", "description": "A long dark hall"}
maze[30][32] = {"type": "hall", "description": "A long dark hall"}
maze[30][33] = {"type": "hall", "description": "A long dark hall"}
maze[30][34] = {"type": "hall", "description": "A long dark hall"}
maze[30][35] = {"type": "hall", "description": "A long dark hall"}
maze[30][36] = {"type": "hall", "description": "A long dark hall"}
maze[30][38] = {"type": "hall", "description": "A long dark hall"}
maze[30][40] = {"type": "hall", "description": "A long dark hall"}

# Row 31 #
maze[31][2] = {"type": "hall", "description": "A long dark hall"}
maze[31][4] = {"type": "hall", "description": "A long dark hall"}
maze[31][6] = {"type": "hall", "description": "A long dark hall"}
maze[31][8] = {"type": "hall", "description": "A long dark hall"}
maze[31][24] = {"type": "hall", "description": "A long dark hall"}
maze[31][32] = {"type": "hall", "description": "A long dark hall"}
maze[31][34] = {"type": "hall", "description": "A long dark hall"}
maze[31][35] = {"type": "hall", "description": "A long dark hall"}
maze[31][36] = {"type": "hall", "description": "A long dark hall"}
maze[31][38] = {"type": "hall", "description": "A long dark hall"}
maze[31][40] = {"type": "hall", "description": "A long dark hall"}

# Row 32 #
maze[32][2] = {"type": "hall", "description": "A long dark hall"}
maze[32][4] = {"type": "hall", "description": "A long dark hall"}
maze[32][6] = {"type": "hall", "description": "A long dark hall"}
maze[32][8] = {"type": "hall", "description": "A long dark hall"}
maze[32][24] = {"type": "hall", "description": "A long dark hall"}
maze[32][32] = {"type": "hall", "description": "A long dark hall"}
maze[32][34] = {"type": "hall", "description": "A long dark hall"}
maze[32][35] = {"type": "hall", "description": "A long dark hall"}
maze[32][36] = {"type": "hall", "description": "A long dark hall"}
maze[32][38] = {"type": "hall", "description": "A long dark hall"}
maze[32][40] = {"type": "hall", "description": "A long dark hall"}

# Row 33 #
maze[33][2] = {"type": "hall", "description": "A long dark hall"}
maze[33][4] = {"type": "hall", "description": "A long dark hall"}
maze[33][6] = {"type": "hall", "description": "A long dark hall"}
maze[33][8] = {"type": "hall", "description": "A long dark hall"}
maze[33][24] = {"type": "hall", "description": "A long dark hall"}
maze[33][32] = {"type": "hall", "description": "A long dark hall"}
maze[33][34] = {"type": "hall", "description": "A long dark hall"}
maze[33][35] = {"type": "hall", "description": "A long dark hall"}
maze[33][36] = {"type": "hall", "description": "A long dark hall"}
maze[33][38] = {"type": "hall", "description": "A long dark hall"}
maze[33][40] = {"type": "hall", "description": "A long dark hall"}

# Row 34 #
maze[34][2] = {"type": "hall", "description": "A long dark hall"}
maze[34][4] = {"type": "hall", "description": "A long dark hall"}
maze[34][5] = {"type": "hall", "description": "A long dark hall"}
maze[34][6] = {"type": "hall", "description": "A long dark hall"}
maze[34][8] = {"type": "hall", "description": "A long dark hall"}
maze[34][9] = {"type": "hall", "description": "A long dark hall"}
maze[34][10] = {"type": "hall", "description": "A long dark hall"}
maze[34][11] = {"type": "hall", "description": "A long dark hall"}
maze[34][12] = {"type": "hall", "description": "A long dark hall"}
maze[34][13] = {"type": "hall", "description": "A long dark hall"}
maze[34][14] = {"type": "hall", "description": "A long dark hall"}
maze[34][15] = {"type": "hall", "description": "A long dark hall"}
maze[34][16] = {"type": "hall", "description": "A long dark hall"}
maze[34][17] = {"type": "hall", "description": "A long dark hall"}
maze[34][18] = {"type": "hall", "description": "A long dark hall"}
maze[34][19] = {"type": "hall", "description": "A long dark hall"}
maze[34][20] = {"type": "hall", "description": "A long dark hall"}
maze[34][21] = {"type": "hall", "description": "A long dark hall"}
maze[34][22] = {"type": "hall", "description": "A long dark hall"}
maze[34][23] = {"type": "hall", "description": "A long dark hall"}
maze[34][24] = {"type": "hall", "description": "A long dark hall"}
maze[34][25] = {"type": "hall", "description": "A long dark hall"}
maze[34][26] = {"type": "hall", "description": "A long dark hall"}
maze[34][27] = {"type": "hall", "description": "A long dark hall"}
maze[34][28] = {"type": "hall", "description": "A long dark hall"}
maze[34][29] = {"type": "hall", "description": "A long dark hall"}
maze[34][30] = {"type": "hall", "description": "A long dark hall"}
maze[34][31] = {"type": "hall", "description": "A long dark hall"}
maze[34][32] = {"type": "hall", "description": "A long dark hall"}
maze[34][34] = {"type": "hall", "description": "A long dark hall"}
maze[34][35] = {"type": "hall", "description": "A long dark hall"}
maze[34][36] = {"type": "hall", "description": "A long dark hall"}
maze[34][38] = {"type": "hall", "description": "A long dark hall"}
maze[34][40] = {"type": "hall", "description": "A long dark hall"}

# Row 35 #
maze[35][2] = {"type": "hall", "description": "A long dark hall"}
maze[35][4] = {"type": "hall", "description": "A long dark hall"}
maze[35][6] = {"type": "hall", "description": "A long dark hall"}
maze[35][8] = {"type": "hall", "description": "A long dark hall"}
maze[35][24] = {"type": "hall", "description": "A long dark hall"}
maze[35][32] = {"type": "hall", "description": "A long dark hall"}
maze[35][34] = {"type": "hall", "description": "A long dark hall"}
maze[35][35] = {"type": "hall", "description": "A long dark hall"}
maze[35][36] = {"type": "hall", "description": "A long dark hall"}
maze[35][38] = {"type": "hall", "description": "A long dark hall"}
maze[35][40] = {"type": "hall", "description": "A long dark hall"}

# Row 36 #
maze[36][2] = {"type": "hall", "description": "A long dark hall"}
maze[36][4] = {"type": "hall", "description": "A long dark hall"}
maze[36][6] = {"type": "hall", "description": "A long dark hall"}
maze[36][7] = {"type": "hall", "description": "A long dark hall"}
maze[36][8] = {"type": "hall", "description": "A long dark hall"}
maze[36][9] = {"type": "hall", "description": "A long dark hall"}
maze[36][10] = {"type": "hall", "description": "A long dark hall"}
maze[36][11] = {"type": "hall", "description": "A long dark hall"}
maze[36][12] = {"type": "hall", "description": "A long dark hall"}
maze[36][13] = {"type": "hall", "description": "A long dark hall"}
maze[36][14] = {"type": "hall", "description": "A long dark hall"}
maze[36][15] = {"type": "hall", "description": "A long dark hall"}
maze[36][16] = {"type": "hall", "description": "A long dark hall"}
maze[36][17] = {"type": "hall", "description": "A long dark hall"}
maze[36][18] = {"type": "hall", "description": "A long dark hall"}
maze[36][19] = {"type": "hall", "description": "A long dark hall"}
maze[36][20] = {"type": "hall", "description": "A long dark hall"}
maze[36][21] = {"type": "hall", "description": "A long dark hall"}
maze[36][22] = {"type": "hall", "description": "A long dark hall"}
maze[36][23] = {"type": "hall", "description": "A long dark hall"}
maze[36][24] = {"type": "hall", "description": "A long dark hall"}
maze[36][25] = {"type": "hall", "description": "A long dark hall"}
maze[36][26] = {"type": "hall", "description": "A long dark hall"}
maze[36][27] = {"type": "hall", "description": "A long dark hall"}
maze[36][28] = {"type": "hall", "description": "A long dark hall"}
maze[36][29] = {"type": "hall", "description": "A long dark hall"}
maze[36][30] = {"type": "hall", "description": "A long dark hall"}
maze[36][31] = {"type": "hall", "description": "A long dark hall"}
maze[36][32] = {"type": "hall", "description": "A long dark hall"}
maze[36][33] = {"type": "hall", "description": "A long dark hall"}
maze[36][34] = {"type": "hall", "description": "A long dark hall"}
maze[36][35] = {"type": "hall", "description": "A long dark hall"}
maze[36][36] = {"type": "hall", "description": "A long dark hall"}
maze[36][38] = {"type": "hall", "description": "A long dark hall"}
maze[36][40] = {"type": "hall", "description": "A long dark hall"}

# Row 37 #
maze[37][2] = {"type": "hall", "description": "A long dark hall"}
maze[37][4] = {"type": "hall", "description": "A long dark hall"}
maze[37][38] = {"type": "hall", "description": "A long dark hall"}
maze[37][40] = {"type": "hall", "description": "A long dark hall"}

# Row 38 #
maze[38][2] = {"type": "hall", "description": "A long dark hall"}
maze[38][4] = {"type": "hall", "description": "A long dark hall"}
maze[38][5] = {"type": "hall", "description": "A long dark hall"}
maze[38][6] = {"type": "hall", "description": "A long dark hall"}
maze[38][7] = {"type": "hall", "description": "A long dark hall"}
maze[38][8] = {"type": "hall", "description": "A long dark hall"}
maze[38][9] = {"type": "hall", "description": "A long dark hall"}
maze[38][10] = {"type": "hall", "description": "A long dark hall"}
maze[38][11] = {"type": "hall", "description": "A long dark hall"}
maze[38][12] = {"type": "hall", "description": "A long dark hall"}
maze[38][13] = {"type": "hall", "description": "A long dark hall"}
maze[38][14] = {"type": "hall", "description": "A long dark hall"}
maze[38][15] = {"type": "hall", "description": "A long dark hall"}
maze[38][16] = {"type": "hall", "description": "A long dark hall"}
maze[38][17] = {"type": "hall", "description": "A long dark hall"}
maze[38][18] = {"type": "hall", "description": "A long dark hall"}
maze[38][19] = {"type": "hall", "description": "A long dark hall"}
maze[38][20] = {"type": "hall", "description": "A long dark hall"}
maze[38][21] = {"type": "hall", "description": "A long dark hall"}
maze[38][22] = {"type": "hall", "description": "A long dark hall"}
maze[38][23] = {"type": "hall", "description": "A long dark hall"}
maze[38][24] = {"type": "hall", "description": "A long dark hall"}
maze[38][25] = {"type": "hall", "description": "A long dark hall"}
maze[38][26] = {"type": "hall", "description": "A long dark hall"}
maze[38][27] = {"type": "hall", "description": "A long dark hall"}
maze[38][28] = {"type": "hall", "description": "A long dark hall"}
maze[38][29] = {"type": "hall", "description": "A long dark hall"}
maze[38][30] = {"type": "hall", "description": "A long dark hall"}
maze[38][31] = {"type": "hall", "description": "A long dark hall"}
maze[38][32] = {"type": "hall", "description": "A long dark hall"}
maze[38][33] = {"type": "hall", "description": "A long dark hall"}
maze[38][34] = {"type": "hall", "description": "A long dark hall"}
maze[38][35] = {"type": "hall", "description": "A long dark hall"}
maze[38][36] = {"type": "hall", "description": "A long dark hall"}
maze[38][37] = {"type": "hall", "description": "A long dark hall"}
maze[38][38] = {"type": "hall", "description": "A long dark hall"}
maze[38][40] = {"type": "hall", "description": "A long dark hall"}

# Row 39 #
maze[39][2] = {"type": "hall", "description": "A long dark hall"}
maze[39][24] = {"type": "hall", "description": "A long dark hall"}
maze[39][40] = {"type": "hall", "description": "A long dark hall"}

# Row 40 #
maze[40][2] = {"type": "hall", "description": "A long dark hall"}
maze[40][3] = {"type": "hall", "description": "A long dark hall"}
maze[40][4] = {"type": "hall", "description": "A long dark hall"}
maze[40][5] = {"type": "hall", "description": "A long dark hall"}
maze[40][6] = {"type": "hall", "description": "A long dark hall"}
maze[40][7] = {"type": "hall", "description": "A long dark hall"}
maze[40][8] = {"type": "hall", "description": "A long dark hall"}
maze[40][9] = {"type": "hall", "description": "A long dark hall"}
maze[40][10] = {"type": "hall", "description": "A long dark hall"}
maze[40][11] = {"type": "hall", "description": "A long dark hall"}
maze[40][12] = {"type": "hall", "description": "A long dark hall"}
maze[40][13] = {"type": "hall", "description": "A long dark hall"}
maze[40][14] = {"type": "hall", "description": "A long dark hall"}
maze[40][15] = {"type": "hall", "description": "A long dark hall"}
maze[40][16] = {"type": "hall", "description": "A long dark hall"}
maze[40][17] = {"type": "hall", "description": "A long dark hall"}
maze[40][18] = {"type": "hall", "description": "A long dark hall"}
maze[40][19] = {"type": "hall", "description": "A long dark hall"}
maze[40][20] = {"type": "hall", "description": "A long dark hall"}
maze[40][21] = {"type": "hall", "description": "A long dark hall"}
maze[40][22] = {"type": "hall", "description": "A long dark hall"}
maze[40][23] = {"type": "hall", "description": "A long dark hall"}
maze[40][24] = {"type": "hall", "description": "A long dark hall"}
maze[40][25] = {"type": "hall", "description": "A long dark hall"}
maze[40][26] = {"type": "hall", "description": "A long dark hall"}
maze[40][27] = {"type": "hall", "description": "A long dark hall"}
maze[40][28] = {"type": "hall", "description": "A long dark hall"}
maze[40][29] = {"type": "hall", "description": "A long dark hall"}
maze[40][30] = {"type": "hall", "description": "A long dark hall"}
maze[40][31] = {"type": "hall", "description": "A long dark hall"}
maze[40][32] = {"type": "hall", "description": "A long dark hall"}
maze[40][33] = {"type": "hall", "description": "A long dark hall"}
maze[40][34] = {"type": "hall", "description": "A long dark hall"}
maze[40][35] = {"type": "hall", "description": "A long dark hall"}
maze[40][36] = {"type": "hall", "description": "A long dark hall"}
maze[40][37] = {"type": "hall", "description": "A long dark hall"}
maze[40][38] = {"type": "hall", "description": "A long dark hall"}
maze[40][39] = {"type": "hall", "description": "A long dark hall"}
maze[40][40] = {"type": "hall", "description": "A long dark hall"}

# Walls #
# Row 3 #
maze[3][3] = {"type": "wall", "description": "It's a wall"}
maze[3][4] = {"type": "wall", "description": "It's a wall"}
maze[3][5] = {"type": "wall", "description": "It's a wall"}
maze[3][6] = {"type": "wall", "description": "It's a wall"}
maze[3][7] = {"type": "wall", "description": "It's a wall"}
maze[3][8] = {"type": "wall", "description": "It's a wall"}
maze[3][9] = {"type": "wall", "description": "It's a wall"}
maze[3][10] = {"type": "wall", "description": "It's a wall"}
maze[3][11] = {"type": "wall", "description": "It's a wall"}
maze[3][12] = {"type": "wall", "description": "It's a wall"}
maze[3][13] = {"type": "wall", "description": "It's a wall"}
maze[3][14] = {"type": "wall", "description": "It's a wall"}
maze[3][15] = {"type": "wall", "description": "It's a wall"}
maze[3][16] = {"type": "wall", "description": "It's a wall"}
maze[3][17] = {"type": "wall", "description": "It's a wall"}
maze[3][18] = {"type": "wall", "description": "It's a wall"}
maze[3][19] = {"type": "wall", "description": "It's a wall"}
maze[3][20] = {"type": "wall", "description": "It's a wall"}
maze[3][21] = {"type": "wall", "description": "It's a wall"}
maze[3][23] = {"type": "wall", "description": "It's a wall"}
maze[3][24] = {"type": "wall", "description": "It's a wall"}
maze[3][25] = {"type": "wall", "description": "It's a wall"}
maze[3][26] = {"type": "wall", "description": "It's a wall"}
maze[3][27] = {"type": "wall", "description": "It's a wall"}
maze[3][28] = {"type": "wall", "description": "It's a wall"}
maze[3][29] = {"type": "wall", "description": "It's a wall"}
maze[3][30] = {"type": "wall", "description": "It's a wall"}
maze[3][31] = {"type": "wall", "description": "It's a wall"}
maze[3][32] = {"type": "wall", "description": "It's a wall"}
maze[3][33] = {"type": "wall", "description": "It's a wall"}
maze[3][34] = {"type": "wall", "description": "It's a wall"}
maze[3][35] = {"type": "wall", "description": "It's a wall"}
maze[3][36] = {"type": "wall", "description": "It's a wall"}
maze[3][37] = {"type": "wall", "description": "It's a wall"}
maze[3][38] = {"type": "wall", "description": "It's a wall"}
maze[3][39] = {"type": "wall", "description": "It's a wall"}

# Row 4 #
maze[4][3] = {"type": "wall", "description": "It's a wall"}
maze[4][39] = {"type": "wall", "description": "It's a wall"}

# Row 5 #
maze[5][3] = {"type": "wall", "description": "It's a wall"}
maze[5][5] = {"type": "wall", "description": "It's a wall"}
maze[5][6] = {"type": "wall", "description": "It's a wall"}
maze[5][7] = {"type": "wall", "description": "It's a wall"}
maze[5][8] = {"type": "wall", "description": "It's a wall"}
maze[5][9] = {"type": "wall", "description": "It's a wall"}
maze[5][10] = {"type": "wall", "description": "It's a wall"}
maze[5][11] = {"type": "wall", "description": "It's a wall"}
maze[5][12] = {"type": "wall", "description": "It's a wall"}
maze[5][13] = {"type": "wall", "description": "It's a wall"}
maze[5][14] = {"type": "wall", "description": "It's a wall"}
maze[5][15] = {"type": "wall", "description": "It's a wall"}
maze[5][16] = {"type": "wall", "description": "It's a wall"}
maze[5][17] = {"type": "wall", "description": "It's a wall"}
maze[5][18] = {"type": "wall", "description": "It's a wall"}
maze[5][19] = {"type": "wall", "description": "It's a wall"}
maze[5][21] = {"type": "wall", "description": "It's a wall"}
maze[5][22] = {"type": "wall", "description": "It's a wall"}
maze[5][23] = {"type": "wall", "description": "It's a wall"}
maze[5][25] = {"type": "wall", "description": "It's a wall"}
maze[5][26] = {"type": "wall", "description": "It's a wall"}
maze[5][27] = {"type": "wall", "description": "It's a wall"}
maze[5][28] = {"type": "wall", "description": "It's a wall"}
maze[5][29] = {"type": "wall", "description": "It's a wall"}
maze[5][30] = {"type": "wall", "description": "It's a wall"}
maze[5][31] = {"type": "wall", "description": "It's a wall"}
maze[5][32] = {"type": "wall", "description": "It's a wall"}
maze[5][33] = {"type": "wall", "description": "It's a wall"}
maze[5][34] = {"type": "wall", "description": "It's a wall"}
maze[5][35] = {"type": "wall", "description": "It's a wall"}
maze[5][36] = {"type": "wall", "description": "It's a wall"}
maze[5][37] = {"type": "wall", "description": "It's a wall"}
maze[5][39] = {"type": "wall", "description": "It's a wall"}

# Row 6 #
maze[6][3] = {"type": "wall", "description": "It's a wall"}
maze[6][5] = {"type": "wall", "description": "It's a wall"}
maze[6][9] = {"type": "wall", "description": "It's a wall"}
maze[6][19] = {"type": "wall", "description": "It's a wall"}
maze[6][21] = {"type": "wall", "description": "It's a wall"}
maze[6][37] = {"type": "wall", "description": "It's a wall"}
maze[6][39] = {"type": "wall", "description": "It's a wall"}

# Row 7 #
maze[7][3] = {"type": "wall", "description": "It's a wall"}
maze[7][5] = {"type": "wall", "description": "It's a wall"}
maze[7][9] = {"type": "wall", "description": "It's a wall"}
maze[7][11] = {"type": "wall", "description": "It's a wall"}
maze[7][12] = {"type": "wall", "description": "It's a wall"}
maze[7][13] = {"type": "wall", "description": "It's a wall"}
maze[7][14] = {"type": "wall", "description": "It's a wall"}
maze[7][15] = {"type": "wall", "description": "It's a wall"}
maze[7][16] = {"type": "wall", "description": "It's a wall"}
maze[7][17] = {"type": "wall", "description": "It's a wall"}
maze[7][19] = {"type": "wall", "description": "It's a wall"}
maze[7][21] = {"type": "wall", "description": "It's a wall"}
maze[7][23] = {"type": "wall", "description": "It's a wall"}
maze[7][24] = {"type": "wall", "description": "It's a wall"}
maze[7][25] = {"type": "wall", "description": "It's a wall"}
maze[7][26] = {"type": "wall", "description": "It's a wall"}
maze[7][27] = {"type": "wall", "description": "It's a wall"}
maze[7][28] = {"type": "wall", "description": "It's a wall"}
maze[7][29] = {"type": "wall", "description": "It's a wall"}
maze[7][30] = {"type": "wall", "description": "It's a wall"}
maze[7][31] = {"type": "wall", "description": "It's a wall"}
maze[7][32] = {"type": "wall", "description": "It's a wall"}
maze[7][33] = {"type": "wall", "description": "It's a wall"}
maze[7][34] = {"type": "wall", "description": "It's a wall"}
maze[7][35] = {"type": "wall", "description": "It's a wall"}
maze[7][37] = {"type": "wall", "description": "It's a wall"}
maze[7][39] = {"type": "wall", "description": "It's a wall"}

# Row 8 #
maze[8][3] = {"type": "wall", "description": "It's a wall"}
maze[8][9] = {"type": "wall", "description": "It's a wall"}
maze[8][11] = {"type": "wall", "description": "It's a wall"}
maze[8][17] = {"type": "wall", "description": "It's a wall"}
maze[8][21] = {"type": "wall", "description": "It's a wall"}
maze[8][23] = {"type": "wall", "description": "It's a wall"}
maze[8][35] = {"type": "wall", "description": "It's a wall"}
maze[8][37] = {"type": "wall", "description": "It's a wall"}
maze[8][39] = {"type": "wall", "description": "It's a wall"}

# Row 9 #
maze[9][3] = {"type": "wall", "description": "It's a wall"}
maze[9][5] = {"type": "wall", "description": "It's a wall"}
maze[9][9] = {"type": "wall", "description": "It's a wall"}
maze[9][11] = {"type": "wall", "description": "It's a wall"}
maze[9][17] = {"type": "wall", "description": "It's a wall"}
maze[9][19] = {"type": "wall", "description": "It's a wall"}
maze[9][21] = {"type": "wall", "description": "It's a wall"}
maze[9][23] = {"type": "wall", "description": "It's a wall"}
maze[9][25] = {"type": "wall", "description": "It's a wall"}
maze[9][26] = {"type": "wall", "description": "It's a wall"}
maze[9][27] = {"type": "wall", "description": "It's a wall"}
maze[9][28] = {"type": "wall", "description": "It's a wall"}
maze[9][29] = {"type": "wall", "description": "It's a wall"}
maze[9][30] = {"type": "wall", "description": "It's a wall"}
maze[9][31] = {"type": "wall", "description": "It's a wall"}
maze[9][32] = {"type": "wall", "description": "It's a wall"}
maze[9][33] = {"type": "wall", "description": "It's a wall"}
maze[9][35] = {"type": "wall", "description": "It's a wall"}
maze[9][37] = {"type": "wall", "description": "It's a wall"}
maze[9][39] = {"type": "wall", "description": "It's a wall"}

# Row 10 #
maze[10][3] = {"type": "wall", "description": "It's a wall"}
maze[10][5] = {"type": "wall", "description": "It's a wall"}
maze[10][9] = {"type": "wall", "description": "It's a wall"}
maze[10][17] = {"type": "wall", "description": "It's a wall"}
maze[10][19] = {"type": "wall", "description": "It's a wall"}
maze[10][21] = {"type": "wall", "description": "It's a wall"}
maze[10][25] = {"type": "wall", "description": "It's a wall"}
maze[10][33] = {"type": "wall", "description": "It's a wall"}
maze[10][35] = {"type": "wall", "description": "It's a wall"}
maze[10][37] = {"type": "wall", "description": "It's a wall"}
maze[10][39] = {"type": "wall", "description": "It's a wall"}

# Row 11 #
maze[11][3] = {"type": "wall", "description": "It's a wall"}
maze[11][5] = {"type": "wall", "description": "It's a wall"}
maze[11][9] = {"type": "wall", "description": "It's a wall"}
maze[11][11] = {"type": "wall", "description": "It's a wall"}
maze[11][17] = {"type": "wall", "description": "It's a wall"}
maze[11][19] = {"type": "wall", "description": "It's a wall"}
maze[11][21] = {"type": "wall", "description": "It's a wall"}
maze[11][23] = {"type": "wall", "description": "It's a wall"}
maze[11][25] = {"type": "wall", "description": "It's a wall"}
maze[11][33] = {"type": "wall", "description": "It's a wall"}
maze[11][35] = {"type": "wall", "description": "It's a wall"}
maze[11][37] = {"type": "wall", "description": "It's a wall"}
maze[11][39] = {"type": "wall", "description": "It's a wall"}

# Row 12 #
maze[12][3] = {"type": "wall", "description": "It's a wall"}
maze[12][5] = {"type": "wall", "description": "It's a wall"}
maze[12][9] = {"type": "wall", "description": "It's a wall"}
maze[12][11] = {"type": "wall", "description": "It's a wall"}
maze[12][17] = {"type": "wall", "description": "It's a wall"}
maze[12][19] = {"type": "wall", "description": "It's a wall"}
maze[12][21] = {"type": "wall", "description": "It's a wall"}
maze[12][23] = {"type": "wall", "description": "It's a wall"}
maze[12][25] = {"type": "wall", "description": "It's a wall"}
maze[12][33] = {"type": "wall", "description": "It's a wall"}
maze[12][35] = {"type": "wall", "description": "It's a wall"}
maze[12][37] = {"type": "wall", "description": "It's a wall"}
maze[12][39] = {"type": "wall", "description": "It's a wall"}

# Row 13 #
maze[13][3] = {"type": "wall", "description": "It's a wall"}
maze[13][5] = {"type": "wall", "description": "It's a wall"}
maze[13][9] = {"type": "wall", "description": "It's a wall"}
maze[13][11] = {"type": "wall", "description": "It's a wall"}
maze[13][12] = {"type": "wall", "description": "It's a wall"}
maze[13][13] = {"type": "wall", "description": "It's a wall"}
maze[13][14] = {"type": "wall", "description": "It's a wall"}
maze[13][15] = {"type": "wall", "description": "It's a wall"}
maze[13][16] = {"type": "wall", "description": "It's a wall"}
maze[13][17] = {"type": "wall", "description": "It's a wall"}
maze[13][19] = {"type": "wall", "description": "It's a wall"}
maze[13][21] = {"type": "wall", "description": "It's a wall"}
maze[13][23] = {"type": "wall", "description": "It's a wall"}
maze[13][25] = {"type": "wall", "description": "It's a wall"}
maze[13][33] = {"type": "wall", "description": "It's a wall"}
maze[13][35] = {"type": "wall", "description": "It's a wall"}
maze[13][37] = {"type": "wall", "description": "It's a wall"}
maze[13][39] = {"type": "wall", "description": "It's a wall"}


# Row 14 #
maze[14][3] = {"type": "wall", "description": "It's a wall"}
maze[14][5] = {"type": "wall", "description": "It's a wall"}
maze[14][9] = {"type": "wall", "description": "It's a wall"}
maze[14][19] = {"type": "wall", "description": "It's a wall"}
maze[14][21] = {"type": "wall", "description": "It's a wall"}
maze[14][23] = {"type": "wall", "description": "It's a wall"}
maze[14][33] = {"type": "wall", "description": "It's a wall"}
maze[14][35] = {"type": "wall", "description": "It's a wall"}
maze[14][39] = {"type": "wall", "description": "It's a wall"}


# Row 15 #
maze[15][3] = {"type": "wall", "description": "It's a wall"}
maze[15][5] = {"type": "wall", "description": "It's a wall"}
maze[15][6] = {"type": "wall", "description": "It's a wall"}
maze[15][7] = {"type": "wall", "description": "It's a wall"}
maze[15][8] = {"type": "wall", "description": "It's a wall"}
maze[15][9] = {"type": "wall", "description": "It's a wall"}
maze[15][10] = {"type": "wall", "description": "It's a wall"}
maze[15][11] = {"type": "wall", "description": "It's a wall"}
maze[15][12] = {"type": "wall", "description": "It's a wall"}
maze[15][13] = {"type": "wall", "description": "It's a wall"}
maze[15][14] = {"type": "wall", "description": "It's a wall"}
maze[15][15] = {"type": "wall", "description": "It's a wall"}
maze[15][16] = {"type": "wall", "description": "It's a wall"}
maze[15][17] = {"type": "wall", "description": "It's a wall"}
maze[15][18] = {"type": "wall", "description": "It's a wall"}
maze[15][19] = {"type": "wall", "description": "It's a wall"}
maze[15][21] = {"type": "wall", "description": "It's a wall"}
maze[15][23] = {"type": "wall", "description": "It's a wall"}
maze[15][25] = {"type": "wall", "description": "It's a wall"}
maze[15][33] = {"type": "wall", "description": "It's a wall"}
maze[15][35] = {"type": "wall", "description": "It's a wall"}
maze[15][37] = {"type": "wall", "description": "It's a wall"}
maze[15][39] = {"type": "wall", "description": "It's a wall"}

# Row 16 #
maze[16][3] = {"type": "wall", "description": "It's a wall"}


'''
maze[1][1] = {"type": "right_turn", "description": "a turn in the path"}
maze[1][2] = {"type": "hall", "description": "A long dark hall"}
maze[1][3] = {"type": "hall", "description": "A long dark hall"}
maze[1][4] = {"type": "hall", "description": "A long dark hall"}
maze[1][5] = {"type": "hall", "description": "A long dark hall"}
maze[1][6] = {"type": "hall", "description": "A long dark hall"}
maze[1][7] = {"type": "hall", "description": "A long dark hall"}
maze[1][8] = {"type": "hall", "description": "A long dark hall"}
maze[1][9] = {"type": "hall", "description": "A long dark hall"}
maze[1][10] = {"type": "hall", "description": "A long dark hall"}
maze[1][11] = {"type": "hall", "description": "A long dark hall"}
maze[1][12] = {"type": "hall", "description": "A long dark hall"}
maze[1][13] = {"type": "hall", "description": "A long dark hall"}
maze[1][14] = {"type": "hall", "description": "A long dark hall"}
maze[1][15] = {"type": "hall", "description": "A long dark hall"}
maze[1][16] = {"type": "hall", "description": "A long dark hall"}
maze[1][17] = {"type": "hall", "description": "A long dark hall"}
maze[1][18] = {"type": "hall", "description": "A long dark hall"}
maze[1][19] = {"type": "right_turn", "description": "A a fork in the road"}
maze[1][20] = {"type": "hall", "description": "A long dark hall"}
maze[1][21] = {"type": "hall", "description": "A long dark hall"}
maze[1][22] = {"type": "hall", "description": "A long dark hall"}
maze[1][23] = {"type": "hall", "description": "A long dark hall"}
maze[1][24] = {"type": "hall", "description": "A long dark hall"}
maze[1][25] = {"type": "hall", "description": "A long dark hall"}
maze[1][26] = {"type": "hall", "description": "A long dark hall"}
maze[1][27] = {"type": "hall", "description": "A long dark hall"}
maze[1][28] = {"type": "hall", "description": "A long dark hall"}
maze[1][29] = {"type": "hall", "description": "A long dark hall"}
maze[1][30] = {"type": "hall", "description": "A long dark hall"}
maze[1][31] = {"type": "hall", "description": "A long dark hall"}
maze[1][32] = {"type": "hall", "description": "A long dark hall"}
maze[1][33] = {"type": "hall", "description": "A long dark hall"}
maze[1][34] = {"type": "hall", "description": "A long dark hall"}
maze[1][35] = {"type": "hall", "description": "A long dark hall"}
maze[1][36] = {"type": "hall", "description": "A long dark hall"}
maze[1][37] = {"type": "right_turn", "description": "A a fork in the road"}
'''


# use this to clear the buffer before sending to the combat function or anything else
def clear_keyboard_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()


# Function to display cell information
def describe_cell(row, col):
    cell = maze[row][col]

    if cell["type"] == "wall":
        print("You can't move there; it's a wall!")
    else:
        # example if statement to display the rooms just change the type == to whatever you
        # need and add the function from room gen and change the type in the maze map cell above
        if cell["type"] == "hall":
            print("\n" * 100)  # python sucks and won't let you cls ugh
            print(cell.get("description",
                           "An empty area."))  # prints the description and says An empty area if it's not filled in
            hallway()
        if "monster" in cell and cell["monster"]:  # calling the combat function with set enemy
            print("you see an enemy here:", ",".join(cell["monster"]))  # debug
            clear_keyboard_buffer()

            main("false", cell["monster"])

        if "monster_rand" in cell and cell["monster_rand"]:
            clear_keyboard_buffer()
            main("true", cell["monster_rand"])
        if "exit" in cell:
            print("exit made it")
            end_game()

        if "items" in cell and cell["items"]:
            print("You see an item here:", ", ".join(cell["items"]))


def move_player(delta_row, delta_col):
    global player_position

    # print(f"Debug: Current player position before moving: {player_position}")  # Debug statement

    new_row = player_position[0] + delta_row
    new_col = player_position[1] + delta_col

    if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
        if maze[new_row][new_col]["type"] != "wall":
            player_position = [new_row, new_col]
            # print(f"Debug: Player moved to new position: {player_position}")  # Debug statement
            describe_cell(new_row, new_col)
        else:
            print("You can't move there; it's a wall!")
    else:
        print("You can't move outside the grid!")


def attempt_pickup():
    """Retrieve the cell at player position and pass it to pick_up_item."""
    current_cell = maze[player_position[0]][player_position[1]]
    pick_up_item(current_cell)
