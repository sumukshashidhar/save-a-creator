# import the necessary libraries
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_video_ids(creator_name, api_key):
    # set up the YouTube API service
    youtube = build('youtube', 'v3', developerKey=api_key)

    # use the search().list() method to get the channel ID for the given creator name
    try:
        response = youtube.search().list(
            part='id',
            q=creator_name,
            type='channel',
            maxResults=1
        ).execute()
        channel_id = response['items'][0]['id']['channelId']
    except HttpError as e:
        print('An error occurred: %s' % e)
        return None

    # use the channels().list() method to get the content details for the given channel
    try:
        response = youtube.channels().list(
            part='contentDetails',
            id=channel_id
        ).execute()
        playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    except HttpError as e:
        print('An error occurred: %s' % e)
        return None

    # use the playlistItems().list() method to get the video IDs for the uploads playlist of the given channel
    try:
        video_ids = []
        playlist_response = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50
        ).execute()
        while playlist_response:
            playlist_items = playlist_response['items']
            for playlist_item in playlist_items:
                video_ids.append(playlist_item['contentDetails']['videoId'])
            if 'nextPageToken' in playlist_response:
                next_page_token = playlist_response['nextPageToken']
                playlist_response = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId=playlist_id,
                    maxResults=50,
                    pageToken=next_page_token
                ).execute()
            else:
                break
    except HttpError as e:
        print('An error occurred: %s' % e)
        return None

    # return the list of video IDs
    return video_ids