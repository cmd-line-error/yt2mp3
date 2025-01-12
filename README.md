Built in Python 3.12.4

Install requirements.txt with pip from main directory.

YOU MUST HAVE FFMPEG INSTALLED TO USE THIS PROGRAM: 

    Install in Main Python Library:
    pip install ffmpeg
    
    Ubuntu and debian (in pkg manager):
    sudo apt-get install ffmpeg

    macOS (using brew):
    brew install ffmpeg

    Windows (using chocolatery):
    choco install ffmpeg

Alternatively, the ffmpeg source can be found at https://github.com/FFmpeg/FFmpeg 

If you manually download the libraries or receive the error below be sure to update ydl_opts with:

    Error: Postprocessing: ffprobe and ffmpeg not found. Please install or provide the path using --fmpeg-location
    
    Update ydl_opts with:
    'ffmpeg_location': 'C:\\location\\to\\ffmpeg\\bin\\ffmpeg.exe',


MAIN PYTHON SCRIPT IS LOCATED IN /pub/yt2mp3.py 
