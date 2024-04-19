from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .utils.calendar import get_calendar_events
from .whatsapp import process_whatsapp_chats
from .llm_process import llm_reply
from .utils.calendar import get_calendar_events
from .spotify import spotify_authorize, extract_data
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
from spotipy.oauth2 import SpotifyOAuth
import spotipy

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


@app.get("/analyze/")
def write_diary():
    chats_list = process_whatsapp_chats("D:\\Coding\\Article Helper\\Backend\\Data\\_chat.txt", "Partha✨💫")
    chats = "\n".join(chats_list)
    events = get_calendar_events()
    if len(events) > 0:
        events = "\n".join([f"{event[0]}: {event[1]}" for event in events])
    response = llm_reply(whatsapp_chats=chats,calendar_events=events)
    # print(result)
    # print(events)
    return {"diary_entry": "response"}



