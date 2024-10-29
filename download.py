from pathlib import Path

import yt_dlp


import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


logging.info('🚀 Main ... ')


video_id = 'mCwaDBYOpT0'
video_url = f'https://www.youtube.com/watch?v={video_id}'


def get_youtube_video_info(url):
    # Configure yt-dlp options
    ydl_opts = {
        'skip_download': True,  # We don't want to download the video
        'extract_flat': 'in_playlist',  # Extract metadata without downloading
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract video info
        info = ydl.extract_info(url, download=False)
        return {
            'title': info.get('title'),
            'description': info.get('description'),
            'upload_date': info.get('upload_date'),
            'uploader': info.get('uploader'),
            'view_count': info.get('view_count'),
            'like_count': info.get('like_count'),
            'dislike_count': info.get('dislike_count'),
            'duration': info.get('duration'),
            'tags': info.get('tags'),
            'categories': info.get('categories'),
        }


video_info = get_youtube_video_info(video_url)

for key, value in video_info.items():
    print(f"{key}: {value}")

file_path = Path(f"samples/{video_id}.txt")

# Open the file in append mode and write new content
with file_path.open('w') as file:
    file.write(video_info['description'])

print(f"Data appended to {file_path}")
description = ''
