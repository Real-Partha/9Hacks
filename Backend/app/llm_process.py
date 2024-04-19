import google.generativeai as genai
from .config import settings

genai.configure(api_key=settings.gemini_api_key)
model = genai.GenerativeModel("gemini-pro")
model.temperature = 0.4

whatsapp_preprompt = "These are the whatsapp chats for today, my chats start with me and the other person's chats start with other person. You can perhaps talk about the conversations I had today as one of the diary entries.\n\n"
calendar_preprompt = "These are the calendar events for today. You can perhaps talk about the events I have today as one of the diary entries.\n\n"
postprompt = "Write a diary entry for today using the above information. Return only text and not markdown or HTML.\n\n"

def llm_reply(whatsapp_chats: str, calendar_events: str):
    response = model.generate_content(whatsapp_preprompt+whatsapp_chats+ calendar_preprompt +calendar_events+postprompt)
    return response.text

