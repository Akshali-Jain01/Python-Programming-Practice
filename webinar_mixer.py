# from pygame import mixer
# mixer.init()
# mixer.music.load("abc.mp3")
# mixer.music.set_volume(10)
# mixer.music.play()
# while(1):
#     print("press 'p' to pause , 'r' to resume")
#         # mixer.init()
#         # mixer.music.load("fire d.mp3")
#         # mixer.music.set_volume(10)
#         # mixer.music.play()
#     print("press 'e' to exit the program")
#     choice1= input("enter your choice")
#     if choice1=='p':
#         mixer.music.pause()
#     elif choice1=='r':
#         mixer.music.unpause()
#     elif choice1=='e':
#         mixer.music.stop()
#         break

import pygame
from moviepy.editor import *
clip = VideoFileClip(r"D:\Botosynthesis\VR Intern\New folder\Acculips-Man.mp4")
clip.preview()
pygame.quit()