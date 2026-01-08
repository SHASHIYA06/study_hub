import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

def get_youtube_client():
    """Get YouTube API client"""
    if not YOUTUBE_API_KEY:
        return None
    return build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


def fetch_educational_videos(topic, grade, limit=5):
    """
    Fetch top educational videos from YouTube
    """
    youtube = get_youtube_client()
    if not youtube:
        return []
    
    try:
        query = f"Class {grade} {topic} educational explanation"
        
        request = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=limit,
            order='relevance',
            relevanceLanguage='en',
            videoDuration='medium',
        )
        
        response = request.execute()
        
        videos = []
        for item in response.get('items', []):
            video_data = {
                'title': item['snippet']['title'],
                'video_id': item['id']['videoId'],
                'thumbnail': item['snippet']['thumbnails']['high']['url'],
                'channel': item['snippet']['channelTitle'],
                'description': item['snippet']['description'],
            }
            videos.append(video_data)
        
        return videos
    
    except HttpError as e:
        print(f"YouTube API Error: {e}")
        return []


def get_video_stats(video_id):
    """
    Get view count and engagement metrics
    """
    youtube = get_youtube_client()
    if not youtube:
        return None
    
    try:
        request = youtube.videos().list(
            part='statistics,contentDetails',
            id=video_id
        )
        response = request.execute()
        
        if response['items']:
            stats = response['items'][0]['statistics']
            return {
                'views': int(stats.get('viewCount', 0)),
                'likes': int(stats.get('likeCount', 0)),
                'comments': int(stats.get('commentCount', 0)),
            }
        return None
    except HttpError as e:
        print(f"YouTube API Error: {e}")
        return None


def prioritize_videos_by_quality(videos):
    """
    Score videos based on channel authority and engagement
    """
    trusted_channels = [
        'Khan Academy',
        'BYJU\'S',
        'Physics Wallah',
        'Amoeba Sisters',
        'CrashCourse',
        'TED-Ed',
    ]
    
    for video in videos:
        score = 0
        if any(channel in video['channel'] for channel in trusted_channels):
            score += 50
        
        stats = get_video_stats(video['video_id'])
        if stats:
            views = stats.get('views', 0)
            if views > 100000:
                score += 30
            elif views > 10000:
                score += 20
        
        video['quality_score'] = score
    
    return sorted(videos, key=lambda x: x.get('quality_score', 0), reverse=True)
