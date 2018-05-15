# VideoMaker

The scripts require that you install the Imagemagick program and the MoviePY module. DownloadAndCompile.py requires PRAW to also be installed. If you were to import all of Moviepy and compile, it would throw an error. I have solved this issue by only importing what I need. If you get an erorr from PRAW, copy and paste the PRAW.ini file from the module files into the directory. 

Compile.py will compile clips ( to a maximum of 10, changeable in file ) with an .mp4 extention into one file. You do not need Reddit API tokens to use this script as it will not download any.

DownloadAndCompile.py will download clips ( to a maximum of 10, changeable in file ) from Gfycat and will compile the clips into one file. You will need Reddit API tokens as the script scrapes subreddits for the Gfycat links. You can change the subreddit name in the file by changing the "subredditName" variable to the name of the subreddit, no r/ needed.
