from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.video.VideoClip import VideoClip, TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.resize import resize
from moviepy.video.compositing.concatenate import concatenate_videoclips
import glob, praw, urllib.request, os, sys, time
clipList, creatorList, downloadList = [], [], []

fileList = glob.glob(os.path.join('./', 'Clip*.mp4'))
for f in fileList:
    os.remove(f)
print("""
 _    ___     __           __  ___      __            
| |  / (_)___/ /__  ____  /  |/  /___ _/ /_____  _____
| | / / / __  / _ \/ __ \/ /|_/ / __ `/ //_/ _ \/ ___/
| |/ / / /_/ /  __/ /_/ / /  / / /_/ / ,< /  __/ /    
|___/_/\__,_/\___/\____/_/  /_/\__,_/_/|_|\___/_/                                                   
Script wrote by u/TheTimebike
""")
time.sleep(3)
client_idAuth = #idAuth here
client_secretAuth = #secretAuth here
reddit = praw.Reddit(client_id=client_idAuth, client_secret=client_secretAuth, user_agent='UserAgent')
subreddit = reddit.subreddit('luciorollouts').top(time_filter='all')
for x in subreddit:
    if x.link_flair_text == 'Rollout':
        if x.url.startswith('https://gfycat.com/'):
            downloadList.append(x.url)
            creatorList.append(x.author)
if len(downloadList) > 100:
    limitNum = 100
else:
    limitNum = len(downloadList)
for x in range(0, limitNum):
    splitUrl = str(downloadList[x]).split('/')
    newUrl = 'https://giant.gfycat.com/' + splitUrl[3] + '.mp4'
    urllib.request.urlretrieve(newUrl,  './Clip{0}.mp4'.format(x + 1))
    print('File {0} wrote to the directory!'.format(x + 1), end='\r')
print('All files wrote to the directory')
globList = glob.glob('./Clip*.mp4')
print(globList)
for x in range(1, len(globList) + 1):
    videoClip = VideoFileClip(str(globList[x - 1])[2:]).fx( resize,(1280, 720)) 
    clipList.append(CompositeVideoClip([videoClip, TextClip('u/' + str(creatorList[x - 1]), fontsize=30, color='white').set_pos(('left', 'top')).set_duration(videoClip.duration)]))
    print('File {0} loaded into memory!'.format(x), end='\r')
print('All files loaded into memory, begining render cycle.')
duration = concatenate_videoclips(clipList, method='compose').duration

# Uncomment this one for audio
#concatenate_videoclips(clipList, method='compose').set_audio(AudioFileClip('Audio.mp3').set_duration(duration)).write_videofile("Rendered.mp4", fps=30)

# Uncomment this one for no audio
#concatenate_videoclips(clipList, method='compose').write_videofile("Rendered.mp4", fps=30)
