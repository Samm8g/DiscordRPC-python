import os
import time
from pypresence import Presence
from dotenv import load_dotenv
from activity_data import rich_presence_content

load_dotenv()

client_id = os.getenv("CLIENT_ID")

if not client_id:
    raise ValueError("CLIENT_ID not found in .env file.")

RPC = Presence(client_id)

try:
    RPC.connect()
    print("Connected to Discord RPC. Press Ctrl+C to stop.")

    rich_presence_content["start"] = int(time.time())

    print("Sending this content to Discord:")
    print(rich_presence_content)

    while True:
        RPC.update(**rich_presence_content)
        time.sleep(15)

except KeyboardInterrupt:
    print("\nKeyboardInterrupt detected. Closing RPC...")
    RPC.close()
    print("RPC connection closed. Exiting.")

except Exception as e:
    print(f"\nAn error occurred: {e}")
