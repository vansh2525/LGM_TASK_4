from moviepy.editor import *

video_clip = VideoFileClip("video_for_task_1.mp4")
video_clip = video_clip.subclip(0,6)
video_clip.write_gif("Task_01.gif",fps = 10)
gif_video_clip = VideoFileClip("Task_01.gif")
gif_video_clip.ipython_display()
