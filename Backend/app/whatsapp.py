from datetime import datetime

def process_whatsapp_chats(file_path, my_name):
    today_date = datetime.now().strftime("%d/%m/%y")
    processed_chats = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into timestamp and message
            parts = line.split('] ')
            if len(parts) < 2:
                continue
            timestamp, message = line.split('] ')
            # print(timestamp, message)
            # Extract the date from the timestamp
            message_date = timestamp.strip('[').split(', ')[0]
            # print(message_date, today_date)
            # Check if the message is from today
            if message_date == today_date:
                # Replace names with "me" or "other person"
                message = message.replace(my_name, 'me').replace('~ ', 'other person: ')
                
                # Append the processed message to the list
                processed_chats.append(f"{timestamp}] {message.strip()}")

    return processed_chats

# Example usage:
# file_path = 'D:\\Coding\\Article Helper\\Backend\\Data\\_chat.txt'
# my_name = 'Partha✨💫'  # Replace with your name
# todays_chats = process_whatsapp_chats(file_path, my_name)

# # Print the processed chats
# for chat in todays_chats:
#     print(chat)

# return todays_chats
