# ClipManager
The goal of this Python application is to provide an enhanced clipboard for your computer. It is designed as a shortcut to quickly save text from your clipboard and then store it in a JSON file for access, which gets loaded back onto your clipboard. This is accesed through a key, I like to assign it to a numerical key for easy of use. When you access any command, it lets you view what already exists on the JSON file for access in alphabetical order, which makes it easy when you use a numerical key.

Running
```python3 main.py COMMAND```

Command to chose from:
- save - Save item from clipboard into a key
- load - Load something from clippy to your clipboard
- list - View the items in clippy
- delete - Delete a key from clippy or ALL to delete all

Usage examples in a Gnome terminal
```
gnome-terminal -e "/usr/bin/python3 /PATH/ClipManager/main.py save"
gnome-terminal -e "/usr/bin/python3 /PATH/ClipManager/main.py load"
gnome-terminal -e "/usr/bin/python3 /PATH/ClipManager/main.py list"
gnome-terminal -e "/usr/bin/python3 /PATH/ClipManager/main.py delete"
```
Saving from your clipboard
![Screenshot from 2022-04-15 14-04-32](https://user-images.githubusercontent.com/99443437/163516474-61a78f31-86c6-4e26-b844-33ab1720be32.png)


Loading from the ClipManager
![Screenshot from 2022-04-15 14-03-31](https://user-images.githubusercontent.com/99443437/163516487-56a08111-f322-44ce-aa81-c3e5ff12369b.png)
