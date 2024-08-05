import json

# Function to load settings from a JSON file
def load_settings():
    try:
        with open('../config/settings.json', 'r') as file:
            settings = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, create default settings
        settings = {
            'theme': 'light',
            'language': 'English',
            'notifications': True
        }
    return settings

# Function to save settings to a JSON file
def save_settings(settings):
    with open('../config/settings.json', 'w') as file:
        json.dump(settings, file, indent=4)

# Function to change settings
def change_settings(settings):
    print("Current Settings:")
    for key, value in settings.items():
        print(f"{key}: {value}")
    
    # Get user input to change settings
    theme = input("Enter new theme (e.g., dark, light): ")
    language = input("Enter new language: ")
    notifications = input("Enable notifications (True/False): ").lower() == 'true'

    # Update settings
    settings['theme'] = theme
    settings['language'] = language
    settings['notifications'] = notifications

    print("Settings updated.")

# Main program
if __name__ == "__main__":
    settings = load_settings()
    change_settings(settings)
    save_settings(settings)
