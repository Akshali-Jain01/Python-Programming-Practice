from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os
from time import *
video_clip = VideoFileClip("Acculips-Man.mp4",)
audio_clip = AudioFileClip("abc.mp3")

final_clip = video_clip.set_audio(audio_clip)

# final_clip.ipython_display()

final_clip.preview()