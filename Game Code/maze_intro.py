import random, time, os, keyboard
from colorama import Fore, Style, init
from music import intro_music

from music import intro_music, music
def maze_intro():
    # Try to maximize the screen with F11
    try:
        keyboard.press('f11')
    except:
        print("Fullscreen toggle with F11 may not work in some environments.")


    DUNGEON_CRAWLER_ASCII = f"""
    {Fore.GREEN}
                                                                   ██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗    ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗ 
                                                                   ██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗  ██║   ██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
                                                                   ██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔██╗ ██║   ██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
                                                                   ██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╗██║   ██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗  
                                                                   ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚████║   ╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
                                                                   ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝  ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝              
    """
    
    # ASCII Art for "BEGIN" (from patorjk.com with Crazy font)
    BEGIN_ASCII = f"""
    {Fore.CYAN}
                                                                                                                ██████╗ ███████╗ ██████╗ ██╗███╗   ██╗
                                                                                                                ██╔══██╗██╔════╝██╔════╝ ██║████╗  ██║
                                                                                                                ██████╔╝█████╗  ██║  ███╗██║██╔██╗ ██║
                                                                                                                ██╔══██╗██╔══╝  ██║   ██║██║██║╚██╗██║
                                                                                                                ██████╔╝███████╗╚██████╔╝██║██║ ╚████║
                                                                                                                ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝
    """
    


    
    

    # Initialize colorama
    init(autoreset=True)

    # Clear the screen (works in most terminal environments)
    os.system('cls' if os.name == 'nt' else 'clear')
    # ASCII Art for "Dungeon Crawler" (from patorjk.com with Crazy font DUNGEON)
    MAZE_SIZE = 4

    # Dynamically determine terminal dimensions
    try:
        WIDTH = os.get_terminal_size().columns
        HEIGHT = os.get_terminal_size().lines
    except OSError:
        WIDTH = 240  # Set a default width if terminal size is unavailable
        HEIGHT = 24  # Set a default height if terminal size is unavailable
    text = "Press enter to play..."
    # Calculate padding to center the text
    padding = (WIDTH - len(text)) // 2

    # Center the text by adding spaces on the left
    centered_text = " " * padding + text
    # Calculate the number of lines in the ASCII art
    ascii_art_lines = DUNGEON_CRAWLER_ASCII.count('\n') + BEGIN_ASCII.count('\n')
    # Calculate vertical padding to center the ASCII art vertically
    vertical_padding = (HEIGHT - ascii_art_lines) + 10
    # Print the ASCII art once in the center
    print('\n' * vertical_padding)  # Add vertical padding
    print(DUNGEON_CRAWLER_ASCII)
    intro_music()
    input(centered_text)# this is the wait to play so we have a "main menue"
    print(BEGIN_ASCII)

    DELAY = 0.1
    EMPTY = ' '
    FORWARD_SLASH = chr(9585)
    BACK_SLASH = chr(9586)



    # Track the start time
    start_time = time.time()
    columns = [FORWARD_SLASH] * (WIDTH // MAZE_SIZE)

    try:
        while True:
            # Check if 10 seconds have passed
            if time.time() - start_time > 5:
                break

            # Set up the slashes in columns:
            for i in range(len(columns)):
                if random.randint(0, 1) == 0:
                    columns[i] = FORWARD_SLASH
                else:
                    columns[i] = BACK_SLASH

            # Calculate horizontal padding for center alignment
            row_width = len(columns) * MAZE_SIZE
            padding = (WIDTH - row_width) // 2

            # Print the columns with horizontal padding for centering:
            for row_num in range(MAZE_SIZE):
                print(EMPTY * padding, end='')  # Add padding for horizontal centering
                for i in range(len(columns)):
                    if columns[i] == FORWARD_SLASH:
                        print(EMPTY * (MAZE_SIZE - row_num - 1) + FORWARD_SLASH + EMPTY * row_num, end='')
                    elif columns[i] == BACK_SLASH:
                        print(EMPTY * row_num + BACK_SLASH + EMPTY * (MAZE_SIZE - row_num - 1), end='')
                print()
                time.sleep(DELAY)

    except KeyboardInterrupt:
        print('Program terminated.')

    finally:
        # Clear the screen to show the final ASCII art centered
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Style.BRIGHT}{Fore.GREEN}end of open credit 5 sec USE W A S D TO MOVE.")
    