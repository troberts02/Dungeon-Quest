import pygame



def stop_intro_music():
    pygame.mixer.music.fadeout(3500) # fadeout over x milliseconds 

def intro_music():

    pygame.mixer.init(frequency=16000)
    pygame.mixer.music.load("intro_music.mp3")
    pygame.mixer.music.play(-1)

def music():
    
    pygame.mixer.init(frequency=16000)
    pygame.mixer.music.load("game_music.mp3")# need to change
    pygame.mixer.music.play(-1)
    
def music_player_death():
    
   pygame.mixer.music.load("PlayerScream.mp3")  # Using MP3 format
   pygame.mixer.music.play()
   pygame.time.delay(3000)
   exit