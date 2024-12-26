import random
from room_generation import hallway, t_shape_hallway, Hallway_lh, hallway_rh, deadend
from combat import main as combat_main
from maze_exit import end_game
from inventory import pick_up_item

GRID_SIZE = 21
player_position = [1, 1]  # Starting position
maze = [[{"type": "wall", "visited": False} for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def generate_solvable_maze():
    """Generate a guaranteed solvable maze using Recursive Backtracking."""
    def carve_path(row, col):
        # Mark the current cell as a hall
        maze[row][col] = {"type": "hall", "description": "A carved path", "visited": False}
        
        # Randomly shuffle the directions to make the maze unpredictable
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        random.shuffle(directions)

        for dr, dc in directions:
            new_row, new_col = row + dr * 2, col + dc * 2  # Move two steps in the direction
            if 1 <= new_row < GRID_SIZE - 1 and 1 <= new_col < GRID_SIZE - 1:
                if maze[new_row][new_col]["type"] == "wall":  # If the new cell is a wall
                    # Carve the intermediate cell
                    maze[row + dr][col + dc] = {"type": "hall", "description": "A carved path", "visited": False}
                    carve_path(new_row, new_col)

    # Start carving from the player's starting position
    carve_path(1, 1)

    # Ensure the exit is accessible by carving a direct path to it
    exit_row, exit_col = GRID_SIZE - 2, GRID_SIZE - 2
    maze[exit_row][exit_col] = {"type": "goal", "description": "The exit of the maze", "visited": False}
    if maze[exit_row - 1][exit_col]["type"] == "wall":  # Ensure connection from above
        maze[exit_row - 1][exit_col] = {"type": "hall", "description": "A carved path", "visited": False}
    if maze[exit_row][exit_col - 1]["type"] == "wall":  # Ensure connection from the left
        maze[exit_row][exit_col - 1] = {"type": "hall", "description": "A carved path", "visited": False}

def add_random_features():
    """Add specific room features like turns and dead ends, ensuring they align with their type."""
    room_types = [
        {"type": "t_room", "description": "A T-shaped intersection"},
        {"type": "left_turn", "description": "A sharp left turn"},
        {"type": "right_turn", "description": "A sharp right turn"},
        {"type": "deadend", "description": "A dead end"},
    ]

    enemy_types = [
    {"type": "enemy", "description": "A menacing enemy awaits!", "monster": ["Mad Wizard"]},
    {"type": "enemy", "description": "A terrifying creature looms", "monster": ["Goblin"]},
    {"type": "enemy", "description": "A skeletal figure rises!", "monster": ["Rampaging Skeleton"]},
    {"type": "enemy", "description": "A giant flaming skull approaches!", "monster": ["Giant Flame Skull"]},
    {"type": "enemy", "description": "A chest with sharp teeth attacks!", "monster": ["Mimic"]},
]


    # Add features to hall cells
    for row in range(1, GRID_SIZE - 1):
        for col in range(1, GRID_SIZE - 1):
            if maze[row][col]["type"] == "hall" and random.random() < 0.2:  # 20% chance to modify
                if random.random() < 0.5:
                    # Ensure room types are set explicitly
                    feature = random.choice(room_types).copy()
                    feature["visited"] = False
                    maze[row][col] = feature
                else:
                    # Ensure enemy types are set explicitly
                    enemy = random.choice(enemy_types).copy()
                    enemy["visited"] = False
                    maze[row][col] = enemy


def describe_cell(row, col):
    cell = maze[row][col]

    if cell["type"] == "wall":
        print("You can't move there; it's a wall!")
        deadend()  # Show the dead-end visualization
        return

    # Mark the current cell as visited
    if not cell["visited"]:
        cell["visited"] = True

    # Display the description of the cell
    if cell["visited"]:
        print(f"(Visited) {cell.get('description', 'An empty area.')}")
    else:
        print(cell.get("description", "An empty area."))

    # Dynamically determine the room type based on surrounding walls
    room_type = determine_room_type(row, col)

    # Display the appropriate hallway image based on the determined room type
    if room_type == "hall":
        hallway()  # Straight hallway
    elif room_type == "t_room":
        t_shape_hallway()  # T-shaped room
    elif room_type == "left_turn":
        Hallway_lh()  # Left turn
    elif room_type == "right_turn":
        hallway_rh()  # Right turn
    elif room_type == "deadend":
        deadend()  # Dead end


    # Check if the player has reached the exit
    if cell["type"] == "goal":
        print("Congratulations! You have reached the end of the maze!")
        end_game()  # Call the end_game function from maze_exit to trigger end credits

    # Handle other events
    if "monster" in cell:
        combat_main("false", cell["monster"])
    if "monster_rand" in cell:
        combat_main("true", cell["monster_rand"])
    if "items" in cell:
        print("You see an item here:", ", ".join(cell["items"]))

def determine_room_type(row, col):
    """Determine the room type based on surrounding walls and open spaces."""
    neighbors = {
        "up": maze[row - 1][col] if row > 0 else {"type": "wall"},
        "down": maze[row + 1][col] if row < GRID_SIZE - 1 else {"type": "wall"},
        "left": maze[row][col - 1] if col > 0 else {"type": "wall"},
        "right": maze[row][col + 1] if col < GRID_SIZE - 1 else {"type": "wall"},
    }

    # Check open spaces (non-wall neighbors)
    open_paths = {direction: cell for direction, cell in neighbors.items() if cell["type"] != "wall"}

    # Determine the room type based on open paths
    if len(open_paths) == 1:
        return "deadend"  # Only one open path
    elif len(open_paths) == 2:
        # Check for straight hallway (aligned open paths)
        if ("up" in open_paths and "down" in open_paths) or ("left" in open_paths and "right" in open_paths):
            return "hall"
        # Otherwise, it's a turn
        if "up" in open_paths and "right" in open_paths:
            return "right_turn"
        if "up" in open_paths and "left" in open_paths:
            return "left_turn"
        if "down" in open_paths and "right" in open_paths:
            return "right_turn"
        if "down" in open_paths and "left" in open_paths:
            return "left_turn"
    elif len(open_paths) == 3:
        return "t_room"  # Three open paths
    elif len(open_paths) == 4:
        return "hall"  # Four open paths (crossroads)

    # Default to a dead end if something goes wrong
    return "deadend"


def move_player(delta_row, delta_col):
    global player_position

    new_row = player_position[0] + delta_row
    new_col = player_position[1] + delta_col

    if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
        if maze[new_row][new_col]["type"] != "wall":
            player_position = [new_row, new_col]
            describe_cell(new_row, new_col)
        else:
            print("You can't move there; it's a wall!")
            deadend() 
    else:
        print("You can't move outside the grid!")


def display_visited_path():
    """Display the maze with visited cells, walls, and the exit."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell = maze[row][col]
            if cell["type"] == "wall":
                print(" # ", end="")  # Wall
            elif cell["type"] == "goal":
                print(" E ", end="")  # Exit
            elif cell["visited"]:
                print(" V ", end="")  # Visited
            else:
                print(" . ", end="")  # Unvisited
        print()  # Newline for grid


def attempt_pickup():
    """Retrieve the cell at player position and pass it to pick_up_item."""
    current_cell = maze[player_position[0]][player_position[1]]
    if "items" in current_cell:
        print(f"You pick up: {', '.join(current_cell['items'])}")
        pick_up_item(current_cell)
    else:
        print("There's nothing to pick up here.")


# Generate the maze and ensure it is solvable
generate_solvable_maze()
add_random_features()
