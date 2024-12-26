# movement_system.py
import os,keyboard, time
# Hides the pygame message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame # import after you hide the message 
from maze_intro import maze_intro 
from music import music, stop_intro_music
from maze import describe_cell, move_player, display_visited_path, attempt_pickup
from inventory import pick_up_item, show_inventory


# Run the maze intro once 
maze_intro()
stop_intro_music()
music()
def check_keypress():
    key_map = {
        'w': 'W', 'a': 'A', 's': 'S', 'd': 'D',
        'i': 'I', 'p': 'P'
    }
    for key in key_map:
        if keyboard.is_pressed(key) or keyboard.is_pressed(key_map[key]):
            return key
    return None


def handle_keypress(key_pressed):
    match key_pressed:
        case 'w':
            move_player(-1, 0)
        case 'a':
            move_player(0, -1)
        case 's':
            move_player(1, 0)
        case 'd':
            move_player(0, 1)
        case 'i':
            show_inventory()
        case 'p':
            attempt_pickup()
        case _:
            print("Unknown key pressed.")

    # Display the visited path (optional)
    display_visited_path()


def main():
    while True:
        key_pressed = check_keypress()
        if key_pressed:
            handle_keypress(key_pressed)
            while keyboard.is_pressed(key_pressed):
                time.sleep(0.01)