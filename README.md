Downloads .mp3 AUDIO ONLY from any YouTube video. 

Built in Python 3.12.4

1. Install requirements.txt with pip from main directory or manually install yt_dlp
2. Install ffmpeg
3. Run /pub/yt2mp3.py


YOU MUST HAVE FFMPEG INSTALLED TO USE THIS PROGRAM: 


    Install in Main Python Library:
    pip install ffmpeg
    
    Debian/Ubuntu/Linux (in pkg manager):
    sudo apt-get install ffmpeg

    MacOS (using brew):
    brew install ffmpeg

    Windows (using chocolatery):
    choco install ffmpeg


Alternatively, the ffmpeg source mirror can be found at https://github.com/FFmpeg/FFmpeg 

If you manually download the ffmpeg libraries or receive the error "Error: Postprocessing: ffprobe and ffmpeg not found. Please install or provide the path using --fmpeg-location"

Update the /pub/yt2mp3.py ydl_opts by adding the following under line 14:


    'ffmpeg_location': 'C:\\location\\to\\ffmpeg\\bin\\ffmpeg.exe',


MAIN PYTHON SCRIPT IS LOCATED IN /pub/yt2mp3.py 
