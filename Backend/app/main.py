from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .utils.calendar import get_calendar_events
from .whatsapp import process_whatsapp_chats
from .llm_process import llm_reply
from .utils.photos import get_google_photos
from .spotify import spotify_authorize, extract_data
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from .schemas import Token, Diary, RetrieveDiary
import pymongo
from datetime import datetime

def connect():
    client = pymongo.MongoClient("mongodb+srv://ashfaqjani21:ninja1215@cluster0.flhjrah.mongodb.net/?retryWrites=true&w=majority")
    db = client["Diary"]
    return db

def insert_diary(email, diary):
    current_date = datetime.now().strftime("%d-%m-%Y")
    # Check if email already exists in the collection
    db = connect()
    collection = db["diaries"]
    result = collection.find_one({"email": email})
    if not result:
        new_entry = {"email": email, "diary": [{"date": current_date, "diary": diary}]}
        collection.insert_one(new_entry)
    else:
        # If email exists, update the document by pushing a new diary entry
        collection.update_one(
            {"email": email},
            {"$push": {"diary": {"date": current_date, "diary": diary}}}
        )

    # If email doesn't exist, create a new document

def retrieve_diary(email):
    db = connect()
    collection = db["diaries"]
    result = collection.find_one({"email": email})
    if result:
        return result["diary"]
    return None



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/analyze/")
def write_diary(token: Diary):
    chats_list = process_whatsapp_chats("D:\\Coding\\Article Helper\\Backend\\Data\\_chat.txt", "Partha✨💫")
    chats = "\n".join(chats_list)
    events = get_calendar_events(token.token)
    if len(events) > 0:
        events = "\n".join([f"{event[0]}: {event[1]}" for event in events])
    # get_google_photos(token.token)
    response = llm_reply(whatsapp_chats=chats,calendar_events=events)
    insert_diary(token.email, response)
    # print(result)
    # print(events)
    # print(token)
    return {"diary_entry": response}

@app.get("/diary/")
def get_diary(data: RetrieveDiary):
    diary = retrieve_diary(data.email)
    if diary:
        return {"diary": diary}
    else:
        raise HTTPException(status_code=404, detail="Diary entry not found")
