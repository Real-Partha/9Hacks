# import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from datetime import datetime
import json

# from google_auth_oauthlib.flow import InstalledAppFlow

# Define the scopes for accessing Calendar data
token_file_path = "D:\\Coding\\Article Helper\\Backend\\app\\token.json"

# if not os.path.exists(token_file_path):
#     SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/photoslibrary.readonly']

#     # Set up the OAuth 2.0 flow for user authentication
#     flow = InstalledAppFlow.from_client_secrets_file(
#         'D:\\Coding\\Article Helper\\Backend\\app\\utils\\client_secret_cred.json',  # Path to your client secret JSON file
#         scopes=SCOPES
#     )
#     credentials = flow.run_local_server(port=0)

#     # Save the credentials for future use
#     with open(token_file_path, 'w') as token:
#         token.write(credentials.to_json())


def get_calendar_events(token):

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
    service = build("calendar", "v3", credentials=credentials)

    # Get the start and end of today
    today = datetime.utcnow().date()
    start_of_day = (
        datetime(today.year, today.month, today.day, 0, 0, 0, 0).isoformat() + "Z"
    )
    end_of_day = (
        datetime(today.year, today.month, today.day, 23, 59, 59, 999999).isoformat()
        + "Z"
    )

    # Call the Calendar API to fetch the events for today
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=start_of_day,
            timeMax=end_of_day,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    # Print the events
    final_evets = []
    if not events:
        # print('No events found for today.')
        return []
    else:
        # print('Events for today:')
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            final_evets.append((start, event["summary"]))
            print(start, event["summary"])

    return final_evets
