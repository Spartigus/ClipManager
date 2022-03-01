'''
Store text from the clipboard for later access

Commands:
- save - Save item from clipboard into a key
- load - Load something from clippy to your clipboard
- list - View the items in clippy
- delete - Delete a key from clippy or ALL to delete all

Design:
This is meant to be attached to keyboard shortcuts for quick access when it
comes to managing your clipboard and text.

Usage:
gnome-terminal -e "/usr/bin/python3 /PATH/ClipManager/main.py save"
gnome-terminal -e "/usr/bin/python3 /PATH/ClipManager/main.py load"
gnome-terminal -e "/usr/bin/python3 /PATH/ClipManager/main.py list"
gnome-terminal -e "/usr/bin/python3 /PATH/ClipManager/main.py delete"

'''

# Imports needed
import sys
import pyperclip
import json
import os

# Making sure the JSON file is stored in the same directory as the script
APP_PATH = os.path.dirname(os.path.realpath(__file__))
SAVED_DATA = APP_PATH + "/clipboard.json"

# This loads the JSON file or creates it if needed, returns the file as "data"
def load_data(filepath):
    try: # If file doesnt exist
        with open(filepath, "r") as f: # stores in f
            data = json.load(f)
            return data
    except:
        return {}

# Saving from your clipboard to the JSON file at a key
def save_data(filepath, data):
    with open(filepath, "w") as f: # f stores file
        json.dump(data, f, sort_keys=True) # Save data to json file as "w" wipes file

# Delete a key from the JSON file
def delete_data(filepath, key):
    # Uses a temp dictionary for storage of resulting filtered data
    tempdict = dict(filter(lambda item: key not in item, data.items()))

    with open(filepath, "w") as f: # f stores file
        json.dump(tempdict, f, sort_keys=True) # Save data to json file as "w" wipes file

# Delete all keys from the JSON file
def delete_all(filepath):
    # Uses a temp dictionary for storage of resulting filtered data
    tempdict = {}

    with open(filepath, "w") as f: # f stores file
        json.dump(tempdict, f) # Save data to json file as "w" wipes file

# User Input
# Handles the argument you can pass it to call from the terminal
if len(sys.argv) == 2:
    # Assign terminal function to a variable
    command = sys.argv[1]

    # Load the JSON file to the data variable
    data = load_data(SAVED_DATA)

    # Managing the save function input
    if command == "save":
        print("ClipManager - Clipboard Extender\n")
        print("----------")
        print("Current Clips:")

        # Loops through the JSON to display what is there already
        for items in data.items():
            print("Key: " + items[0] + "\nClip: \n" + items[1] + "\n")
        print("----------")
        print("Clip to save: \n", pyperclip.paste())

        # Getting the user key and saving it to the JSON file
        key = input("\nType the key for this clip: ")
        data[key] = pyperclip.paste()##
        save_data(SAVED_DATA, data)
        print("Data that was saved: ", pyperclip.paste())

    # Managing the list function input
    elif command == "list":

        # Displaying the items in the file
        print("ClipManager - Clipboard Extender\n")
        print("----------")
        print("Current Clips:")
        for items in data.items():
            print("Key: " + items[0] + "\nClip: \n" + items[1] + "\n")

        # Stalls the exiting of the terminal for viewer to read
        print("----------")
        close = input("Hit enter to continue")

    # Managing the load function input
    elif command == "load":

        # Displaying the data in the JSON file to prompt user
        print("ClipManager - Clipboard Extender\n")
        print("----------")
        print("Load a key:")
        for items in data.items():
            print("Key: " + items[0] + "\nClip: \n" + items[1] + "\n")

        # Getting the key to load and loading it to your clipboard
        print("----------")
        key = input("Type the key to load the clip into your clipboard: ")
        if key in data:
            pyperclip.copy(data[key])
            print("Data loaded to clipboard: ", pyperclip.paste())

        # Handle a key that doesn't exist
        else:
            print("Key does not exist")

    # Managing the delete function input
    elif command == "delete":

        # Display the keys that can be deleted
        print("ClipManager - Clipboard Extender\n")
        print("----------")
        print("Current Clips:")
        for items in data.items():
            print("Key: " + items[0] + "\nClip: \n" + items[1] + "\n")

        # Taking the key to delete and deleting it from the JSON
        print("----------")
        delkey = input("Type the key to delete the clip or type 'All' to delete all: ")
        if delkey in data:
            print("Deleting: ", delkey)
            delete_data(SAVED_DATA, delkey)

        # Handling the dlete all keys function
        elif delkey == "ALL":
            print("Deleting ALL")
            delete_all(SAVED_DATA)
        else:
            print("Key not in clipboard")

    # Handling an incorrect input
    else:
        print("Unknown command, type either save, load, list or delete")

# Handling an incorrect input
else:
    print("Unknown command, type either save, load, list or delete")
