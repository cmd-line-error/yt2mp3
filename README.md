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

If you manually download the ffmpeg libraries or receive the error "Error: Postprocessing: ffprobe and ffmpeg not found. Please install or provide the path using --fmpeg-location"

Update the /pub/yt2mp3.py ydl_opts by adding the following under line 14:


    'ffmpeg_location': 'C:\\location\\to\\ffmpeg\\bin\\ffmpeg.exe',


MAIN PYTHON SCRIPT IS LOCATED IN /pub/yt2mp3.py 
