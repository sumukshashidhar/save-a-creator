import os

def download_youtube_video(video_id, folder_path, ytdlp_path):
    """
    This function downloads a YouTube video from YouTube in the best quality possible using the yt-dlp command-line utility,
    given a YouTube video ID, and saves the video to a specified folder, with the original video title, appended to the video ID.

    Args:
    video_id (str): The YouTube video ID of the video to be downloaded.
    folder_path (str): The path of the folder where the downloaded video should be saved.
    ytdlp_path (str): The path to the yt-dlp executable.

    Returns:
    None
    """
    # Construct the URL of the video with the specified video ID
    url = f"https://www.youtube.com/watch?v={video_id}"

    # Set options for the downloader
    ytdl_options = f"--format 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]' --output '{os.path.join(folder_path, f'%(title)s-{video_id}.%(ext)s')}' --write-sub --write-auto-sub --sub-lang en"

    # Download the video with the specified video ID and options
    os.system(f"{ytdlp_path} {url} {ytdl_options}")