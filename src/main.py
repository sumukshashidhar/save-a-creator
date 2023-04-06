from get_video_list import get_video_ids
from load_env_vars import load_env_file
from download_video import download_youtube_video

# read env vars
env_vars = load_env_file('.ENV')
creator = env_vars['USERNAME']
api_key = env_vars['API_KEY']
output_folder = env_vars['OUTPUT_PATH']
yt_dl_path = env_vars['YTDLPATH']

# get video IDs
video_ids = get_video_ids(creator, api_key)

# download videos
for video_id in video_ids:
    print("Downloading video with ID: " + video_id)
    download_youtube_video(video_id, output_folder, yt_dl_path)