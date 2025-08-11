# DiscordRPC-python

A simple and customizable Python script to set a custom Discord Rich Presence using the `pypresence` library.
This project is built with best practices in mind, separating data from logic and securely managing credentials.

## Features

  * **Custom Status**: Easily set your custom status messages (`state`, `details`).
  * **Dynamic Timer**: Display a timer counting up since the script started.
  * **External Images**: Use external image URLs or local assets for your profile artwork.
  * **Configurable Activity Type**: Change the activity type to "Playing," "Watching," "Listening to," etc.
  * **Clickable Buttons**: Add up to two clickable buttons with custom labels and URLs.
  * **Secure Credentials**: Uses a `.env` file to store your Discord Client ID, keeping it out of your code.
  * **Clean Structure**: Rich Presence data is stored in a separate `activity_data.py` file for easy modification.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Samm8g/DiscordRPC-python.git
    cd DiscordRPC-python
    ```
2.  **Install dependencies**:
    ```bash
    pip install pypresence python-dotenv
    ```
3.  **Set up your Discord Application**:
      * Go to the [Discord Developer Portal](https://discord.com/developers/applications).
      * Create a new application and copy your **Application ID**.
4.  **Configure the `.env` file**:
      * Rename the `.env.example` file to **`.env`**.
      * Open the new `.env` file and paste your Application ID into it.
    ```ini
    CLIENT_ID=YOUR_APPLICATION_ID
    ```

## Usage

To run the script and activate your custom Rich Presence, simply run the `main.py` file.

```bash
python3 main.py
```

Press `Ctrl+C` in the terminal to stop the script and close the Rich Presence.

## Configuration

All of your Rich Presence content is defined in the `activity_data.py` file.
Open this file to customize your status message, images, buttons, and more.
Read more from activity_data_example.py.txt

```python
# activity_data.py

rich_presence_content = {
    "state": "I'm a developer!",
    "details": "Working on: My Cool Project",
    "activity_type": 0, # 0, 2, 3, 5
    "large_image": "https://example.com/image.png/",
    "large_text": "Text to see when hovering",
    "start": None, # will configured on main.py
    "buttons": [
        {"label": "Button 1", "url": "https://example.com/"},
        {"label": "Button 2", "url": "https://example.com/"}
    ]
}
```

# License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute this code for personal or commercial use. See the [LICENSE](LICENSE) file for the full text.
