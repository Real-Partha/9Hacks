import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from datetime import datetime, timedelta

# Function to extract songs and their categories for today
# def extract_spotify_data(client_id, client_secret):
#     # Authenticate with Spotify API
#     client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
#     sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#     # Get today's date
#     today_date = datetime.now().strftime('%Y-%m-%d')

#     # Get the user's recently played tracks
#     results = sp.current_user_recently_played(limit=50)  # Change limit if needed
#     today_tracks = []

#     # Iterate through the tracks and extract relevant information
#     for item in results['items']:
#         track = item['track']
#         played_at = item['played_at']

#         # Check if the track was played today
#         if played_at.startswith(today_date):
#             track_name = track['name']
#             artist_name = track['artists'][0]['name']  # Assume only one artist for simplicity
#             album_name = track['album']['name']
#             category = sp.artist(track['artists'][0]['id'])['genres']  # Get artist genres

#             # Append the track info to the list
#             today_tracks.append({
#                 'name': track_name,
#                 'artist': artist_name,
#                 'album': album_name,
#                 'category': category
#             })

#     return today_tracks

def spotify_authorize(client_id, client_secret):
    # Authenticate with Spotify API and request necessary scope
    print("Inside Authentication")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,redirect_uri="http://localhost:8000/callback", scope="user-read-recently-played"))

    # Get today's date
    # today_date = datetime.now().strftime('%Y-%m-%d')

    # # Get the user's recently played tracks
    # results = sp.current_user_recently_played(limit=50)  # Change limit if needed
    # today_tracks = []

    # # Iterate through the tracks and extract relevant information
    # for item in results['items']:
    #     track = item['track']
    #     played_at = item['played_at']

    #     # Check if the track was played today
    #     if played_at.startswith(today_date):
    #         track_name = track['name']
    #         artist_name = track['artists'][0]['name']  # Assume only one artist for simplicity
    #         album_name = track['album']['name']
    #         category = sp.artist(track['artists'][0]['id'])['genres']  # Get artist genres

    #         # Append the track info to the list
    #         today_tracks.append({
    #             'name': track_name,
    #             'artist': artist_name,
    #             'album': album_name,
    #             'category': category
    #         })

    # return today_tracks

def extract_data(access_token):
    sp = spotipy.Spotify(auth=access_token)

    # Calculate the date 2 days ago
    two_days_ago = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')

    # Get the user's recently played tracks within the last 2 days
    results = sp.current_user_recently_played(limit=50, after=two_days_ago)
    tracks = []

    for item in results['items']:
        track = item['track']
        played_at = item['played_at']

        # Append the track information to the list
        tracks.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'played_at': played_at
        })
    print("Tracks: ", tracks)
    return tracks

# Example usage:
# if __name__ == "__main__":
#     # Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your actual Spotify credentials
#     client_id = 'YOUR_CLIENT_ID'
#     client_secret = 'YOUR_CLIENT_SECRET'
    
#     today_tracks = extract_spotify_data(client_id, client_secret)

#     # Print the extracted tracks
#     for i, track in enumerate(today_tracks, 1):
#         print(f"Track {i}:")
#         print(f"Name: {track['name']}")
#         print(f"Artist: {track['artist']}")
#         print(f"Album: {track['album']}")
#         print(f"Category: {', '.join(track['category']) if track['category'] else 'Unknown'}")
#         print()
