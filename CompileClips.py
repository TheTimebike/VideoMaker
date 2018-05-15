from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.video.VideoClip import VideoClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.resize import resize
from moviepy.video.compositing.concatenate import concatenate_videoclips
import glob, urllib.request, os, sys, time
clipList, creatorList, downloadList = [], [], []
print("""
 _    ___     __           __  ___      __            
| |  / (_)___/ /__  ____  /  |/  /___ _/ /_____  _____
| | / / / __  / _ \/ __ \/ /|_/ / __ `/ //_/ _ \/ ___/
| |/ / / /_/ /  __/ /_/ / /  / / /_/ / ,< /  __/ /    
|___/_/\__,_/\___/\____/_/  /_/\__,_/_/|_|\___/_/     
                                                      
Script wrote by u/TheTimebike
""")
time.sleep(3)
globList = glob.glob('./*.mp4')
print(globList)
for x in range(1, len(globList) + 1):
    videoClip = VideoFileClip(str(globList[x - 1])[2:]).fx( resize,(1280, 720)) 
    clipList.append(videoClip)
    if x == 10:
        break
    print('File {0} loaded into memory!'.format(x), end='\r')
print('All files loaded into memory, begining render cycle.')
duration = concatenate_videoclips(clipList, method='compose').duration

# Uncomment this one for audio
#concatenate_videoclips(clipList, method='compose').set_audio(AudioFileClip('Audio.mp3').set_duration(duration)).write_videofile("Rendered.mp4", fps=30)

# Uncomment this one for no audio
#concatenate_videoclips(clipList, method='compose').write_videofile("Rendered.mp4", fps=30)
