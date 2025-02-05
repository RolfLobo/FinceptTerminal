import json
import os

SETTINGS_DIR = os.path.join(os.path.expanduser("~"), ".fincept")
SETTINGS_FILE = os.path.join(SETTINGS_DIR, "FinceptSettingModule.json")

def load_settings():
    """
    Load FinceptSettingModule from the FinceptSettingModule.json file.
    If the file does not exist, create it with default empty content.
    """
    if not os.path.exists(SETTINGS_FILE):
        # Create the file with an empty JSON object
        with open(SETTINGS_FILE, "w") as file:
            json.dump({}, file)

    with open(SETTINGS_FILE, "r") as file:
        return json.load(file)

def save_user_data(data):
    """
    Save user data to the FinceptSettingModule.json file.
    """
    settings = load_settings()
    settings.update(data)
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)  # Use indent for better readability

def is_registered():
    """
    Check if a user is registered by verifying the presence of 'name' in FinceptSettingModule.
    """
    settings = load_settings()
    return "username" in settings

def get_user_name():
    """
    Get the registered user's name, or return 'Guest' if no user is registered.
    """
    settings = load_settings()
    return settings.get("username", "Guest")

def clear_user_data():
    """
    Clear all user data by deleting the FinceptSettingModule.json file.
    """
    if os.path.exists(SETTINGS_FILE):
        os.remove(SETTINGS_FILE)