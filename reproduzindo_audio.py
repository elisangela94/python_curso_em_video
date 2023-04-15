#Abri e reproduzir audio 
import os
from moviepy.editor import VideoFileClip

video_path = "C:/Users/Satel/Videos/Captures/izabel 4-11.mp4" # usar barras inclinadas (/) ou barras duplas invertidas (\\)
video = VideoFileClip(video_path).subclip(50, 60)

video.preview()
