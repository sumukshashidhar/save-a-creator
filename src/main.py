from get_video_list import get_video_ids
from load_env_vars import load_env_file

# read env vars
env_vars = load_env_file('.ENV')
creator = env_vars['USERNAME']
api_key = env_vars['API_KEY']

# get video IDs
video_ids = get_video_ids(creator, api_key)

# print video IDs
print(video_ids)