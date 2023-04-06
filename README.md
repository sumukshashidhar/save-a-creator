
# Save-A-Creator: 

A Python script to download YouTube videos from a creator's channel and save them to your local machine.

## Table of Contents

- Introduction
- Requirements
- Installation
- Usage
- License


## Introduction
Save-A-Creator is a Python script that enables you to download all the videos from a YouTube creator's channel and save them to your local machine. It uses the YouTube Data API to fetch the list of video IDs from the creator's channel and the yt-dlp command-line utility to download the videos with the specified video IDs.

## Requirements
- Python 3.6 or higher
- Google API Client Library for Python (google-api-python-client)
- yt-dlp command-line utility


## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using pip:
```python
pip install google-api-python-client
```
3. Download the yt-dlp executable from the official website: https://github.com/yt-dlp/yt-dlp/releases
4. Copy the yt-dlp executable to a directory on your system path, or specify the path to the executable in the .ENV file (see Usage section).
5. Create a new .ENV file in the root directory of the repository and add the following environment variables:
```makefile
USERNAME=<your YouTube username>
API_KEY=<your Google API key>
OUTPUT_PATH=<path to the folder where the downloaded videos should be saved>
YTDLPATH=<path to the yt-dlp executable>
```
6. Save the .ENV file.


## Usage

To use Save-A-Creator:

Open a terminal window and navigate to the root directory of the repository.

Run the following command to download the videos:
```bash
python main.py
```

This will fetch the list of video IDs from the specified creator's channel and download each video in the best available quality (with a maximum resolution of 720p) to the specified OUTPUT_PATH folder. The videos will be saved with their original title and the video ID appended to the filename.

Note: If you specified the path to the yt-dlp executable in the .ENV file, make sure to use the correct path in the YTDLPATH variable.

Wait for the script to complete. The progress of the download will be displayed in the console.

## License
This project is licensed under the MIT License - see the LICENSE file for details.