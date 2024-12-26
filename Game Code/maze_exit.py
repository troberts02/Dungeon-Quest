import sys, time, os, random, msvcrt
from colorama import Fore, Style, init

def clear_keyboard_buffer():
    print("made it")
    while msvcrt.kbhit():
        msvcrt.getch()



CONGRATULATIONS_ASCII = f"""
    {Fore.GREEN}
                                  ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗██╗   ██╗██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗     
                                 ██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝     
                                 ██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║███████╗      
                                 ██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║      
                                 ╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║
                                  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝                                                               
                                                                                 
    """

 

def end_game():

    clear_keyboard_buffer()
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
   
    clear_keyboard_buffer()
    text = "Press enter to close..."
    # Calculate padding to center the text
    padding = (WIDTH - len(text)) // 2

    # Center the text by adding spaces on the left
    centered_text = " " * padding + text
    print(CONGRATULATIONS_ASCII)
    input(centered_text)
    
    print("GG - nathanael")
    print("GG - Trey")
    time.sleep(.5)
    sys.exit()