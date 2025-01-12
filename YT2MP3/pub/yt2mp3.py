import os
import yt_dlp

def download_video(video_url, output_path="downloads", video_format="best"):
    """
    Downloads a YouTube video using yt-dlp.

    Args:
        video_url (str): The URL of the YouTube video to download.
        output_path (str): The directory where the video will be saved.
        video_format (str): The format in which to download the video (e.g., 'best', 'worst').
    """
    # Define download options
    ydl_opts = {
        'referer': 'https://www.youtube.com',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save with video title and extension
        'noplaylist': True,  # Download only the video, not a playlist
        'quiet': False,  # Show download progress
        'progress_hooks': [progress_hook],  # Add a hook to track progress
    }

    # Download the video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        print(f"Error: {e}")

def progress_hook(d):
    """
    Progress hook to display download status.

    Args:
        d (dict): Progress data.
    """
    if d['status'] == 'finished':
        print(f"Done downloading: {d['filename']}")
    elif d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} of {d['_total_bytes_str']} at {d['_speed_str']}")

if __name__ == "__main__":
    # Example usage
    url = input("Enter the YouTube video URL: ")
    output_directory = input("Enter the output directory (default: 'downloads'): ") or "downloads"
    download_video(video_url=url, output_path=output_directory)
