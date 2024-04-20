from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json

def get_google_photos(token):

    with open('D:\\Coding\\Article Helper\\Backend\\app\\token.json', 'r') as file:
        data = json.load(file)

    # Step 2: Manipulate the dictionary
    data['token'] = token

    # Step 3: Write the updated dictionary back to the JSON file
    with open("D:\\Coding\\Article Helper\\Backend\\app\\token.json", 'w') as file:
        json.dump(data, file, indent=4)

    # Load credentials from token.json
    credentials = Credentials.from_authorized_user_file('D:\\Coding\\Article Helper\\Backend\\app\\token.json')

    # Build the Calendar API service
    try:
        service = build("photoslibrary", "v1", credentials=credentials)

        # Define search criteria (can be further customized)
        search_query = ''  # Optional: Filter by filename, date, etc.

        results = service.mediaItems().search(body={'pageSize': 2, 'searchTerm': search_query}).execute()
        photos = results.get('mediaItems', [])

        if not photos:
            print('No photos found in the user\'s library.')
        else:
            for photo in photos:
                # Access photo details (URL, filename, etc.) using photo['baseUrl'] or other properties
                print(f"Photo details: {photo}")

    except Exception as error:
        print(f"An error occurred: {error}")