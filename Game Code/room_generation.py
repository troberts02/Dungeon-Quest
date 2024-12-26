def t_shape_hallway():
    ascii_Art = """
                ____________________________________________________________________________________________________________________________________________
                |                                        \                                                        /                                        |
                |                                         \                                                      /                                         |
                |                                          \                                                    /                                          |
                |                                           \                                                  /                                           |
                |                                            \                                                /                                            |
                |                                             \                                              /                                             |
                |                                              \                                            /                                              |
                |                                               \__________________________________________/                                               |
                |                                               |                                          |                                               |
                |                                               |                                          |                                               |
                |                                               |                                          |                                               |
                |                                               |                                          |                                               |
                |                                               | ^                   ^                  ^ |                                               |
                |                                               |  )                 ( )                (  |                                               |
                |                                               | █                   █                  █ |                                               |
                |                                               |                                          |                                               |
                |                                ^              |                ┌─────────┐               |              ^                                |
                |                               ( )             |                │  <--->  │               |             ( )                               |
                |                ^               █              |                └─────────┘               |              █               ^                |
                |               ( )                             |____________________│ │___________________|                             ( )               |
                |^               █                              |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|                              █               ^|
                | )                                             |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|                                             ( |
                |█                                              |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|                                              █|
                |                                               |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|                                               |
                |                                               /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                               |
                |                                              /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                              |
                |                                             /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                             |
                |                                            /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                            |
                |                                           /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                           |
                |                                          /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                          |
                |                                         /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                         |
                ____________________________________________________________________________________________________________________________________________
                """
    print(ascii_Art)



def hallway():
    asci_Art = """
                _____________________________________________________________________________________________________________________________________________
                |                                        \                                                         /                                        |
                |                                         \                                                       /                                         |
                |                                          \                                                     /                                          |
                |                                           \                                                   /                                           |
                |                                            \                                                 /                                            |
                |                                             \                                               /                                             |
                |                                              \                                             /                                              |
                |                                               \                                           /                                               |
                |                                                \                                         /                                                |
                |                                                 \                                       /                                                 |
                |                                                  \                                     /                                                  |
                |                                                   \                                   /                                                   |
                |                                                    ___________________________________                                                    |
                |                                                    |                                 |                                                    |
                |                                                 ^  |                                 |  ^                                                 |
                |                                                ( ) |                                 | ( )                                                |
                |                                 ^               █  |                                 |  █               ^                                 |
                |                                ( )                 |                                 |                 ( )                                |
                |                 ^               █                  |                                 |                  █               ^                 |
                |                ( )                                 ___________________________________                                 ( )                |
                | ^               █                                /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                 █               ^ |
                |  )                                              /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                               (  |
                | █                                              /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                               █ |
                |                                               /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                                |
                |                                              /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                               |
                |                                             /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                              |
                |                                            /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                             |
                |                                           /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                            |
                |                                          /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                           |
                |                                         /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                          |
                |                                        /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                         |
                _____________________________________________________________________________________________________________________________________________
                """
    print(asci_Art)  # Print the ASCII art


def Hallway_lh():
    asci_ari = """
                    _____________________________________________________________________________________________________________________________________________
                    |                                        \                                                         /                                        |
                    |                                         \                                                       /                                         |
                    |                                          \                                                     /                                          |
                    |                                           \                                                   /                                           |
                    |                                           |\                                                 /                                            |
                    |                                           | \                                               /                                             |
                    |                                           |  \                                             /                                              |
                    |                                           |   \                                           /                                               |
                    |                                           |   |\                                         /                                                |   
                    |                                           |   | \                                       /                                                 |
                    |                                           |   |  \                                     /                                                  |
                    |                                           |   |   \                                   /                                                   |
                    |                                           |   |    ___________________________________                                                    |
                    |                                           |   |    |                                 |                                                    |
                    |                                           |   | ^  |                                 |  ^                                                 |
                    |                                           |   |( ) |                                 | ( )                                                |
                    |                                 ^         |   | █  |                                 |  █               ^                                 |
                    |                                ( )        |   |    |                                 |                 ( )                                |
                    |                  ^              █         |   |    ┌─────────┐                       |                  █               ^                 |
                    |                 ( )                       |   |   /│     ^   │________________________                                 ( )                |
                    | ^                █                        |   |  /░│   <─┘   │░░░░░░░░░░░░░░░░░░░░░░░░\                                 █               ^ |
                    |  )                                        |   | /░░└─────────┘░░░░░░░░░░░░░░░░░░░░░░░░░\                                               (  |
                    | █                                         |   |/░░░░░░░│ │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                               █ |
                    |                                           |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                                |
                    |                                           |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                               |
                    |                                           |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                              |
                    |                                           |/░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                             |
                    |                                           /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                            |
                    |                                          /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                           |
                    |                                         /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                          |
                    |                                        /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                         |
                    _____________________________________________________________________________________________________________________________________________
                    """
    
    print(asci_ari)

def hallway_rh():
    asci_ari ="""
                _____________________________________________________________________________________________________________________________________________
                |                                        \                                                         /                                        |
                |                                         \                                                       /                                         |
                |                                          \                                                     /                                          |
                |                                           \                                                   /                                           |
                |                                            \                                                 /|                                           |
                |                                             \                                               / |                                           |
                |                                              \                                             /  |                                           |
                |                                               \                                           /   |                                           |
                |                                                \                                         /|   |                                           |
                |                                                 \                                       / |   |                                           |
                |                                                  \                                     /  |   |                                           |
                |                                                   \                                   /   |   |                                           |
                |                                                    ___________________________________    |   |                                           |
                |                                                    |                                 |    |   |                                           |
                |                                                 ^  |                                 |  ^ |   |                                           |
                |                                                ( ) |                                 | ( )|   |                                           |
                |                                 ^               █  |                                 |  █ |   |          ^                                |
                |                                ( )                 |                                 |    |   |         ( )                               |
                |                ^                █                  |                      ┌─────────┐|    |   |          █               ^                |
                |               ( )                                  _______________________│   ^     │_    |   |                         ( )               |
                |^               █                                  /░░░░░░░░░░░░░░░░░░░░░░░│   └─>   │░\   |   |                          █               ^|
                | )                                                /░░░░░░░░░░░░░░░░░░░░░░░░└─────────┘░░\  |   |                                         ( |
                |█                                                /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│ │░░░░░░░\ |   |                                          █|
                |                                                /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\|   |                                           |
                |                                               /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|                                           |
                |                                              /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|                                           |
                |                                             /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|                                           |
                |                                            /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|                                           |
                |                                           /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                           |
                |                                          /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                          |
                |                                         /░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\                                         |
                ---------------------------------------------------------------------------------------------------------------------------------------------
                
                """

    print(asci_ari)

def deadend():
    asci_art="""
                _____________________________________________________________________________________________________________________________________________
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |       
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |              ^                             ^                                                 ^                             ^              |
                |             ( )                           ( )                                               ( )                           ( )             |
                |              █                             █                                                 █                             █              |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                |                                                                                                                                           |
                _____________________________________________________________________________________________________________________________________________

     """
    print(asci_art)
